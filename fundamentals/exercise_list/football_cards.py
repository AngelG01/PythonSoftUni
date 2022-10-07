team_a = 11
team_b = 11

players_sent_off = input()
players_separated = set(players_sent_off.split())

for curr_player in players_separated:
    if curr_player[0] == "A":
        if team_a < 7:
            break
        team_a -= 1

    else:
        if team_b < 7:
            break
        team_b -= 1

if team_a < 7 or team_b < 7:
    print(f"Team A - {team_a}; Team B - {team_b}")
    print("Game was terminated")
else:
    print(f"Team A - {team_a}; Team B - {team_b}")
