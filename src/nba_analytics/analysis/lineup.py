"""
The function's input is a players dataframe in Box Score
It's output is a dictionary of starting lineups for each team in the game
"""

def get_starting_lineups(players):
    starters = players[
        players["position"].fillna("").str.strip()!=""
    ]

    lineups = {}

    for team, group in starters.groupby("teamTricode"):
        player_ids = set(group["personId"].astype(int))

        if len(player_ids) != 5:
            raise ValueError(
                f"{team}: Expected 5 starters, got {len(player_ids)}"
            )

        lineups[team] = player_ids

    return lineups

# Extract the dictionary of the team players
def build_name_to_id(players, team):
    team_players = players[players['teamTricode'] == team]
    if team_players['familyName'].duplicated().any():
        raise ValueError(f"Duplicate familyName detected for {team}")
    name_to_id_series  = team_players.set_index('familyName')['personId']
    name_to_id = name_to_id_series.to_dict()
    normalized_name_to_id = {
        normalize_name(name): player_id
        for name, player_id in name_to_id.items()
    }
    if len(normalized_name_to_id) != len(name_to_id):
        raise ValueError("Name collision detected")
    return normalized_name_to_id

def parse_substitution(description):
    # The format of description is "SUB: A FOR B"
    parts = description.split(" FOR ")
    player_out = parts[1]
    player_in = parts[0][5:]

    return (player_in, player_out)

def normalize_name(name):
    # Normalize the name to remove accents and special characters
    import unicodedata
    normalized = unicodedata.normalize("NFKD", name)
    return "".join(c for c in normalized if not unicodedata.category(c) == "Mn")

# Track the current lineup for each team
class LineupTracker:
    # Initialization 
    def __init__(self, team, starters):
        self.team = team
        self.on_court = set(starters) # Create an independent set
        # Using set to ensure uniquness 
        if len(self.on_court)!=5:
            raise ValueError('The on_court must contain exactly 5 players ')

    def substitute(self, player_in, player_out):
        if player_out not in self.on_court:
            raise ValueError(f"Player {player_out} is not on the court")
        if player_in in self.on_court:
            raise ValueError(f"Player {player_in} is already on the court")
        # Carry out the substitution
        self.on_court.remove(player_out)
        self.on_court.add(player_in)

    def get_lineup(self):
        # Return an immutable snapshot of the current lineup
        # Here we use frozenset to ensure that the returned lineup cannot be modified
        return frozenset(self.on_court)

def infer_quarter_starters(quarter_subs):
    seen_players = set()
    quarter_starters = set()

    for index, row in quarter_subs.iterrows():
        player_in, player_out = parse_substitution(row["description"])

        if player_out not in seen_players:
            quarter_starters.add(player_out)

        seen_players.add(player_in)
        seen_players.add(player_out)

    return quarter_starters

def get_lineup_at_time(rotation_df, time):
    active_players = rotation_df[
        (rotation_df["IN_TIME_REAL"] <= time) &
        (rotation_df["OUT_TIME_REAL"] > time)
    ]

    player_ids = active_players["PERSON_ID"].tolist()
    
    lineup = frozenset(player_ids)

    return lineup