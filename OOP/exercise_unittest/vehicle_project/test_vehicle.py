from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.car = Vehicle(100, 100)

    def test_init(self):
        self.assertEqual(self.car.fuel, 100)
        self.assertEqual(self.car.capacity, 100)
        self.assertEqual(self.car.horse_power, 100)
        self.assertEqual(self.car.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_error(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(1000)
        self.assertEqual(str(context.exception), "Not enough fuel")

    def test_drive_fine(self):
        self.car.drive(12)
        self.assertEqual(self.car.fuel, 85)

    def test_fuel_error(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(1000)
        self.assertEqual(str(context.exception), "Too much fuel")

    def test_refuel_is_fine(self):
        self.car.drive(12)
        self.car.refuel(10)
        self.assertEqual(self.car.fuel, 95)

    def test_print(self):
        self.assertEqual(str(self.car),
                         f"The vehicle has {self.car.horse_power} horse power with {self.car.fuel} fuel left and {self.car.fuel_consumption} fuel consumption")


if __name__ == '__main__':
    main()
