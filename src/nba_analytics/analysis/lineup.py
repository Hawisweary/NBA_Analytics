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

