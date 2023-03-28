class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed

car = Car("a", "b", 1, 4)
car.make = ""
print(car)


import unittest

class TestCar(unittest.TestCase):

    def test_init(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual(car.make, "a")
        self.assertEqual(car.model, "b")
        self.assertEqual(car.fuel_consumption, 1)
        self.assertEqual(car.fuel_capacity, 4)
        self.assertEqual(car.fuel_amount, 0)

    def test_make(self):
        with self.assertRaises(Exception):
            car = Car("", "b", 1, 4)

    def test_model(self):
        with self.assertRaises(Exception):
            car = Car("a", "", 1, 4)

    def test_fuel_consumption(self):
        with self.assertRaises(Exception):
            car = Car("a", "b", 0, 4)

    def test_fuel_capacity(self):
        with self.assertRaises(Exception):
            car = Car("a", "b", 1, 0)

    def test_fuel_amount(self):
        with self.assertRaises(Exception):
            car = Car("a", "b", 1, 4)
            car.fuel_amount = -1

    def test_refuel(self):
        car = Car("a", "b", 1, 4)
        car.refuel(2)
        self.assertEqual(car.fuel_amount, 2)

    def test_refuel_exception(self):
        car = Car("a", "b", 1, 4)
        with self.assertRaises(Exception):
            car.refuel(-1)

    def test_refuel_capacity(self):
        car = Car("a", "b", 1, 4)
        car.refuel(5)
        self.assertEqual(car.fuel_amount, 4)

    def test_drive(self):
        car = Car("a", "b", 1, 4)
        car.refuel(2)
        car.drive(100)
        self.assertEqual(car.fuel_amount, 1)

    def test_drive_exception(self):
        car = Car("a", "b", 1, 4)
        with self.assertRaises(Exception):
            car.drive(100)
if __name__ == '__main__':
    unittest.main()
