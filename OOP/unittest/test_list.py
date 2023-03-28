class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class TestIntegerList(unittest.TestCase):

    def test_initialization(self):
        my_list = IntegerList(1, 2, 3, 4, 5)
        self.assertEqual(my_list.get_data(), [1, 2, 3, 4, 5])



import unittest

class TestIntegerList(unittest.TestCase):

    def setUp(self):
        self.int_list = IntegerList(1, 2, 3)

    def test_add(self):
        self.int_list.add(4)
        self.assertEqual(self.int_list.get_data(), [1, 2, 3, 4])
        with self.assertRaises(ValueError):
            self.int_list.add('a')

    def test_remove_index(self):
        removed = self.int_list.remove_index(1)
        self.assertEqual(removed, 2)
        self.assertEqual(self.int_list.get_data(), [1, 3])
        with self.assertRaises(IndexError):
            self.int_list.remove_index(2)

    def test_get(self):
        self.assertEqual(self.int_list.get(0), 1)
        with self.assertRaises(IndexError):
            self.int_list.get(3)

    def test_insert(self):
        self.int_list.insert(1, 5)
        self.assertEqual(self.int_list.get_data(), [1, 5, 2, 3])
        with self.assertRaises(IndexError):
            self.int_list.insert(4, 6)
        with self.assertRaises(ValueError):
            self.int_list.insert(1, 'a')

    def test_get_biggest(self):
        self.assertEqual(self.int_list.get_biggest(), 3)

    def test_get_index(self):
        self.assertEqual(self.int_list.get_index(2), 1)
        with self.assertRaises(ValueError):
            self.int_list.get_index('a')

if __name__ == '__main__':
    unittest.main()
