class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):

    def setUp(self) -> None:
        self.cat = Cat('Fluffy')

    def test_cat_size_increase(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_is_it_fed(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cant_eat_more(self):
        self.cat.eat()
        with self.assertRaises(Exception) as context:
            self.cat.eat()
        self.assertEqual(str(context.exception), 'Already fed.')

    def test_cant_fall_asleep(self):
        with self.assertRaises(Exception) as context:
            self.cat.sleep()
        self.assertEqual(str(context.exception), 'Cannot sleep while hungry')

    def test_is_it_sleepy(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
