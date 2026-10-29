from nba_analytics.analysis.lineup import LineupTracker

dal_starters = {
    1642843,  # Flagg
    1629023,  # Washington
    1629655,  # Gafford
    1631108,  # Christie
    202681    # Irving
}

dal = LineupTracker("DAL", dal_starters)

print(dal.get_lineup())

dal.substitute(1643516, 1629655)

print(dal.get_lineup())

# Check Johnson Jr. is on court
assert 1643516 in dal.get_lineup(), "Johnson Jr. should be on the court"

# Check Gafford is off court
assert 1629655 not in dal.get_lineup(), "Gafford should be off"

# Check that the lineup still has 5 players
assert len(dal.get_lineup()) == 5, "Lineup  still have exactly 5 players after substitution"

# Second Substitution: Irving out, Marshall in
dal.substitute(1630230, 202681)

assert 1630230 in dal.get_lineup(), "Player 1630230 should be on the court"
assert 202681 not in dal.get_lineup(), "Player 202681 should be off the court"

print("Final lineup:", dal.get_lineup())