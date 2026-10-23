from nba_api.stats.endpoints import boxscoretraditionalv3

GAME_ID = "0022600091"

box = boxscoretraditionalv3.BoxScoreTraditionalV3(
    game_id=GAME_ID,
    timeout=30
)

players = box.player_stats.get_data_frame()

print("Columns:")
print(players.columns.tolist())

print("\nPlayers and positions:")
print(
    players[
        ["teamTricode", "personId", "nameI", "position"]
    ].to_string(index=False)
)

import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root / "src"))

from nba_analytics.analysis.lineup import get_starting_lineups

starting_lineups = get_starting_lineups(players)

for team, lineup in starting_lineups.items():
    print(team, lineup)