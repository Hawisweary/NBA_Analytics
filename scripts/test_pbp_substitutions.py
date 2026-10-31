from nba_api.stats.endpoints import playbyplayv3
from nba_analytics.analysis.lineup import parse_substitution
from nba_api.stats.endpoints import boxscoretraditionalv3
from nba_analytics.analysis.lineup import build_name_to_id, normalize_name, LineupTracker, get_starting_lineups


GAME_ID = "0022600091"

pbp = playbyplayv3.PlayByPlayV3(
    game_id=GAME_ID,
    start_period=1,
    end_period=4
)

box = boxscoretraditionalv3.BoxScoreTraditionalV3(
    game_id=GAME_ID,
    timeout=30
)

players = box.player_stats.get_data_frame()

pbp_df = pbp.play_by_play.get_data_frame()

print("Total events:", len(pbp_df))

subs = pbp_df[
    pbp_df['actionType'] == "Substitution"
]

print("Total substitutions:", len(subs))

print(
    subs[["period", "clock", "teamTricode", "description"]].head(10)
)

q2 = pbp_df[
    pbp_df["period"] == 2
]

print(
    q2[
        ["clock", "teamTricode", "playerName", "description", "actionType"]
    ].head(20).to_string(index=False)
)

dal_name_to_id = build_name_to_id(players, "DAL")
hou_name_to_id = build_name_to_id(players, "HOU")

starting_lineups = get_starting_lineups(players)

dal_tracker = LineupTracker("DAL", starting_lineups["DAL"])
hou_tracker = LineupTracker("HOU", starting_lineups["HOU"])

for index,row in subs.iterrows():
    description = row['description']
    player_in, player_out = parse_substitution(description)
    team = row['teamTricode']
    if team == "DAL":
        name_to_id = dal_name_to_id
        tracker = dal_tracker
    elif team == "HOU":
        name_to_id = hou_name_to_id
        tracker = hou_tracker
    else:
        raise ValueError(f"Unknown team: {team}")

    player_in_id = name_to_id[player_in]
    player_out_id = name_to_id[player_out]
    '''
    # Update the lineup tracker
    print("---- Substitution ----")
    print("Period:", row["period"])
    print("Clock:", row["clock"])
    print("Team:", team)
    print("IN:", player_in, player_in_id)
    print("OUT:", player_out, player_out_id)
    print("Current lineup:", tracker.get_lineup())
    tracker.substitute(player_in_id, player_out_id)
    '''
    # Verify lineup size
    assert len(tracker.get_lineup()) == 5

    print(team, player_in_id, player_out_id)
'''
Test the character of the name "Bogdanović" to see if it is normalized correctly
import unicodedata

name = "Bogdanović"

for char in unicodedata.normalize("NFKD", name):
    print(repr(char), unicodedata.category(char))
'''
assert normalize_name("Bogdanović") == 'Bogdanovic'

assert normalize_name("Cissé") == 'Cisse'

assert normalize_name("Gafford") == 'Gafford'
