from nba_analytics.analysis.lineup import parse_substitution

description = "SUB: Johnson Jr. FOR Gafford"

player_in, player_out = parse_substitution(description)

print("Player IN:", player_in)
print("Player OUT:", player_out)
assert (player_in, player_out) == ("Johnson Jr.", "Gafford")

description2 = "SUB: Marshall FOR Irving"

# Call your function and unpack the result
player_in2, player_out2 = parse_substitution(description2)

print("Player IN:", player_in2)
print("Player OUT:", player_out2)

# Check the result using assert
assert (player_in2, player_out2) == ("Marshall", "Irving"), f"Expected ('Marshall', 'Irving'), but got ({player_in2}, {player_out2})"