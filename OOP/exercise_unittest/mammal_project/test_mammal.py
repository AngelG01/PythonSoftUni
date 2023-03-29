from unittest import TestCase, main

from OOP.exercise_unittesting.mammal.project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Rashko', 'Dog', 'Woof')

    def test_init(self):
        self.assertEqual(self.mammal.name, 'Rashko')
        self.assertEqual(self.mammal.type, 'Dog')
        self.assertEqual(self.mammal.sound, 'Woof')

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), f"{self.mammal.name} makes {self.mammal.sound}")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_info(self):
        self.assertEqual(self.mammal.info(), f"{self.mammal.name} is of type {self.mammal.type}")


if __name__ == '__main__':
    main()
