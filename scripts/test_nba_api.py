from nba_api.stats.endpoints import leaguegamefinder

# Find NBA games played on October 21, 2026
games = leaguegamefinder.LeagueGameFinder(
    date_from_nullable = "10/21/2026",
    date_to_nullable = "10/21/2026",
    league_id_nullable = "00",
    timeout = 30
).get_data_frames()[0]

# Filter for Dallas Mavericks games
dal_games = games[
    games["MATCHUP"].str.contains("DAL", na=False)
]

print(
    dal_games[
        ["GAME_ID", "GAME_DATE", "MATCHUP", "WL"]
    ].to_string(index = False)
)