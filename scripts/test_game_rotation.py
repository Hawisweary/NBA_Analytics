from nba_api.stats.endpoints import gamerotation
from nba_analytics.analysis.lineup import get_lineup_at_time

GAME_ID = "0022600091"

rotation = gamerotation.GameRotation(game_id=GAME_ID, timeout=30)

print(rotation.get_data_frames()[0].head())
print(rotation.get_data_frames()[1].head())

dal_rotation = rotation.get_data_frames()[0]
hou_rotation = rotation.get_data_frames()[1]


q2_start = 7200

dal_q2 = dal_rotation[
    (dal_rotation["IN_TIME_REAL"] <= q2_start) &
    (dal_rotation["OUT_TIME_REAL"] > q2_start)
]

print(
    dal_rotation[
        ["PLAYER_LAST", "IN_TIME_REAL", "OUT_TIME_REAL"]
    ].head(15).to_string(index=False)
)


hou_q2 = hou_rotation[
    (hou_rotation["IN_TIME_REAL"] <= q2_start) &
    (hou_rotation["OUT_TIME_REAL"] > q2_start)
]

print(
    hou_rotation[
        ["PLAYER_LAST", "IN_TIME_REAL", "OUT_TIME_REAL"]
    ].head(15).to_string(index=False)
)
print(
    hou_q2[
        ["PLAYER_LAST", "PERSON_ID", "IN_TIME_REAL", "OUT_TIME_REAL"]
    ].to_string(index=False)
)

print("DAL Q2 players:", len(dal_q2))
print("HOU Q2 players:", len(hou_q2))

dal_q2_lineup = get_lineup_at_time(dal_rotation, 7200)
hou_q2_lineup = get_lineup_at_time(hou_rotation, 7200)

print("DAL Q2:", dal_q2_lineup)
print("HOU Q2:", hou_q2_lineup)
assert len(dal_q2_lineup) == 5
assert len(hou_q2_lineup) == 5

dal_q3_lineup = get_lineup_at_time(dal_rotation, 14400)
hou_q3_lineup = get_lineup_at_time(hou_rotation, 14400)

dal_q4_lineup = get_lineup_at_time(dal_rotation, 21600)
hou_q4_lineup = get_lineup_at_time(hou_rotation, 21600)

print("DAL Q3:", dal_q3_lineup)
print("HOU Q3:", hou_q3_lineup)
print("DAL Q4:", dal_q4_lineup)
print("HOU Q4:", hou_q4_lineup)

in_times = dal_rotation["IN_TIME_REAL"].tolist()
out_times = dal_rotation["OUT_TIME_REAL"].tolist()

all_times = in_times + out_times

unique_times = sorted(set(all_times))

print(unique_times[:20])