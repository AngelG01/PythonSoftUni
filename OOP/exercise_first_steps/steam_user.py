class SteamUser:
    played_hours = 0

    def __init__(self, username: str, games: list):
        self.username = username
        self.games = games

    def play(self, name: str, hours: int):
        if name in self.games:
            SteamUser.played_hours += hours
            return f'{self.username} is playing {name}'
        else:
            return f"{name} is not in library"


    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            return f'{self.username} bought {game}'
        else:
            return f'{game} is already in your library'


    def status(self):
        return f'{self.username} has {len(self.games)} games. Total play time: {SteamUser.played_hours}'


user = SteamUser("Peter", ["Rainbow SixSiege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())