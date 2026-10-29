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

def parse_substitution(description):
    # The format of description is "SUB: A FOR B"
    parts = description.split(" FOR ")
    player_out = parts[1]
    player_in = parts[0][5:]

    return (player_in, player_out)


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
