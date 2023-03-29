from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.superman = Hero('Superman', 1, 100, 100)
        self.enemy = Hero('Losh', 1, 50, 50)

    def test_init(self):
        self.assertEqual(self.superman.username, 'Superman')
        self.assertEqual(self.superman.level, 1)
        self.assertEqual(self.superman.health, 100)
        self.assertEqual(self.superman.damage, 100)

    def test_fight_with_yourself(self):
        with self.assertRaises(Exception) as context:
            self.superman.battle(self.superman)
        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_health_is_negative(self):
        self.superman.health = -1
        with self.assertRaises(Exception) as context:
            self.superman.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_health_is_zero(self):
        self.superman.health = 0
        with self.assertRaises(Exception) as context:
            self.superman.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_enemy_health_is_negative(self):
        self.enemy.health = -1
        with self.assertRaises(Exception) as context:
            self.superman.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(context.exception))

    def test_enemy_health_is_zero(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as context:
            self.superman.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(context.exception))

    def test_is_it_draw(self):
        self.superman.health = self.enemy.health
        self.superman.damage = self.enemy.damage

        result = self.superman.battle(self.enemy)

        self.assertEqual(0, self.superman.health)
        self.assertEqual(0, self.enemy.health)
        self.assertEqual('Draw', result)

    def test_you_win(self):
        result = self.superman.battle(self.enemy)

        self.assertEqual('You win', result)
        self.assertEqual(self.superman.level, 2)
        self.assertEqual(self.superman.health, 55)
        self.assertEqual(self.superman.damage, 105)

    def test_you_lose(self):
        self.superman.health = 49
        self.superman.damage = 15

        result = self.superman.battle(self.enemy)

        self.assertEqual('You lose', result)
        self.assertEqual(self.enemy.level, 2)
        self.assertEqual(self.enemy.health, 40)
        self.assertEqual(self.enemy.damage, 55)

    def test_string_method(self):
        self.assertEqual(str(self.superman),
                         f"Hero {self.superman.username}: {self.superman.level} lvl\n"f"Health: {self.superman.health}\n"f"Damage: {self.superman.damage}\n")


if __name__ == '__main__':
    main()
