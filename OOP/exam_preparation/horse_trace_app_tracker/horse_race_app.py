from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def find_jockey(self, jockey_name):
        for j in self.jockeys:
            if j.name == jockey_name:
                return j
        else:
            raise Exception(f'Jockey {jockey_name} could not be found!')

    def find_horse(self, horse_type):
        for horse in reversed(self.horses):
            if horse.__class__.__name__ == horse_type and horse.is_taken is False:
                return horse

        raise Exception(f'Horse breed {horse_type} could not be found!')

    def find_horse_race(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race

        raise Exception(f'Race {race_type} could not be found!')

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        for horse in self.horses:
            if horse_name == horse.name:
                raise Exception(f'Horse {horse_name} has been already added!')

        if horse_type == 'Appaloosa':
            horse = Appaloosa(horse_name, horse_speed)
            self.horses.append(horse)
            return f'{horse_type} horse {horse_name} is added.'

        elif horse_type == 'Thoroughbred':
            horse = Thoroughbred(horse_name, horse_speed)
            self.horses.append(horse)
            return f'{horse_type} horse {horse_name} is added.'

    def add_jockey(self, jockey_name: str, age: int):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f'Jockey {jockey_name} has been already added!')

        jock = Jockey(jockey_name, age)
        self.jockeys.append(jock)
        return f'Jockey {jockey_name} is added.'

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f'Race {race_type} has been already created!')
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f'Race {race_type} is created.'

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        curr_jockey = self.find_jockey(jockey_name)
        curr_horse = self.find_horse(horse_type)

        if curr_jockey.horse is not None:
            return f'Jockey {curr_jockey.name} already has a horse.'

        curr_jockey.horse = curr_horse
        curr_horse.is_taken = True

        return f'Jockey {curr_jockey.name} will ride the horse {curr_horse.name}.'

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        curr_race = self.find_horse_race(race_type)
        curr_jockey = self.find_jockey(jockey_name)

        if curr_jockey.horse is None:
            raise Exception(f'Jockey {curr_jockey.name} cannot race without a horse!')

        if curr_jockey in curr_race.jockeys:
            return f'Jockey {curr_jockey.name} has been already added to the {curr_race.race_type} race.'

        curr_race.jockeys.append(curr_jockey)
        return f'Jockey {curr_jockey.name} added to the {curr_race.race_type} race.'

    def start_horse_race(self, race_type: str):
        race = self.find_horse_race(race_type)

        if len(race.jockeys) < 2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')

        highest_speed = 0
        winner = object

        for jockey in race.jockeys:
            if jockey.horse.speed > highest_speed:
                winner = jockey
                highest_speed = jockey.horse.speed

        return f"The winner of the {race.race_type} race, with a speed of {highest_speed}km/h is {winner.name}! " \
               f"Winner's horse: {winner.horse.name}."
