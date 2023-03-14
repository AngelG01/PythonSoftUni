from OOP.exercise_polymorphism.wild_farm.project.animals.animal import Bird
from OOP.exercise_polymorphism.wild_farm.project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    @property
    def gained_weight(self):
        return 0.25

    @staticmethod
    def make_sound():
        return 'Hoot Hoot'

    @property
    def food_that_eats(self):
        return [Meat]


class Hen(Bird):

    @property
    def gained_weight(self):
        return 0.35

    @property
    def food_that_eats(self):
        return [Meat, Vegetable, Fruit, Seed]

    @staticmethod
    def make_sound():
        return 'Cluck'
