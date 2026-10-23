from nba_api.stats.endpoints import playbyplayv3

GAME_ID = "0022600091"

# Fetch play_by_play data
pbp = playbyplayv3.PlayByPlayV3(
    game_id = GAME_ID,
    start_period = 1,
    end_period = 4,
    timeout = 30
)

# Convert the response to a DataFrame
df_pbp = pbp.play_by_play.get_data_frame()

# Inspect the data

print("Total events:", len(df_pbp))
print("\nColumns:")
print(df_pbp.columns.tolist())

print("\nFirst 10 events:")
print(df_pbp.head(10).to_string(index=False))

print("\n=== Columns ===")
print(df_pbp.columns.tolist())

print("\n=== Action Types ===")
print(df_pbp["actionType"].value_counts())

print("\n=== Substitutions ===")
subs = df_pbp[
    df_pbp["actionType"].astype(str).str.contains(
        "substitution", case=False, na=False
    )
]

print(subs.head(15).to_string(index=False))

# Filter events containing scoreboard updates
scores = df_pbp[
    (df_pbp["scoreHome"].astype(str).str.strip() != "") &
    (df_pbp["scoreAway"].astype(str).str.strip() != "")
].copy()

# Convert scores to numeric values
scores["scoreHome"] = scores["scoreHome"].astype(int)
scores["scoreAway"] = scores["scoreAway"].astype(int)

# Display the last 10 score records
print("\n=== Final Score Records ===")

print(
    scores[
        ["period", "clock", "actionNumber",
         "scoreHome", "scoreAway", "description"]
    ].tail(10).to_string(index=False)
)

print("\nFinal score:")
print("HOU:", scores.iloc[-1]["scoreHome"])
print("DAL:", scores.iloc[-1]["scoreAway"])