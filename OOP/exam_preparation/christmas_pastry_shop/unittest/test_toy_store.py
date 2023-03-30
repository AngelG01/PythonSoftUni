from unittest import TestCase, main

from project.toy_store import ToyStore


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_if_shelf_non_exists(self):
        with self.assertRaises(Exception) as content:
            self.toy_store.add_toy('Z', 'Azis')
        self.assertEqual("Shelf doesn't exist!", str(content.exception))

    def test_if_toy_is_already_in_shelf(self):
        self.toy_store.add_toy('A', 'Azis')
        with self.assertRaises(Exception) as content:
            self.toy_store.add_toy('A', 'Azis')
        self.assertEqual('Toy is already in shelf!', str(content.exception))

    def test_if_shelf_is_empty(self):
        self.toy_store.add_toy('A', 'Azis')
        with self.assertRaises(Exception) as content:
            self.toy_store.add_toy('A', 'Azi')
        self.assertEqual('Shelf is already taken!', str(content.exception))

    def test_add_toy(self):
        self.assertEqual(f'Toy:Azis placed successfully!', self.toy_store.add_toy('A', 'Azis'))
        self.assertEqual(self.toy_store.toy_shelf['A'], 'Azis')

    def test_is_shelf_exist_in_remove(self):
        with self.assertRaises(Exception) as content:
            self.toy_store.remove_toy('Z', 'Azi')
        self.assertEqual("Shelf doesn't exist!", str(content.exception))

    def test_is_toy_exist_in_remove(self):
        with self.assertRaises(Exception) as content:
            self.toy_store.remove_toy('A', 'Azi')
        self.assertEqual("Toy in that shelf doesn't exists!", str(content.exception))

    def test_remove_toy(self):
        self.toy_store.add_toy('A', 'Azis')
        self.assertEqual(f"Remove toy:Azis successfully!", self.toy_store.remove_toy('A', 'Azis'))
        self.assertEqual(self.toy_store.toy_shelf['A'], None)


if __name__ == '__main__':
    main()
