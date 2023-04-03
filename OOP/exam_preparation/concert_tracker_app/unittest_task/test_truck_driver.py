from unittest import TestCase, main

from unittest_project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver('Angel', 15.5)

    def test_init(self):
        self.assertEqual('Angel', self.driver.name)
        self.assertEqual(15.5, self.driver.money_per_mile)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_money(self):
        with self.assertRaises(Exception) as err:
            self.driver.earned_money = -1

        self.assertEqual(f"{self.driver.name} went bankrupt.", str(err.exception))

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("California", 2000)

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_added_cargo_error(self):
        self.driver.add_cargo_offer('Sofia', 100)
        with self.assertRaises(Exception) as err:
            self.driver.add_cargo_offer('Sofia', 100)
        self.assertEqual("Cargo offer is already added.", str(err.exception))

    def test_add_cargo_offer(self):
        test1 = self.driver.add_cargo_offer('Sofia', 100)
        self.assertEqual(f"Cargo for 100 to Sofia was added as an offer.", test1)

    def test_none_best_cargo_offer(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual('There are no offers available.', result)

    def test_valid_best_cargo_offer(self):
        self.driver.add_cargo_offer('Sofia', 150)
        self.driver.add_cargo_offer('Varna', 160)

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual('Angel is driving 160 to Varna.', result)
        self.assertEqual(2480, self.driver.earned_money)
        self.assertEqual(160, self.driver.miles)

    def test_eat(self):
        self.driver.earned_money = 100
        self.driver.eat(250)

        self.assertEqual(80, self.driver.earned_money)

    def test_sleep(self):
        self.driver.earned_money = 1000
        self.driver.sleep(1000)
        self.assertEqual(955, self.driver.earned_money)

    def test_pump_gas(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(1500)

        self.assertEqual(500, self.driver.earned_money)

    def test_repair_truck(self):
        self.driver.earned_money = 10000
        self.driver.repair_truck(10000)

        self.assertEqual(2500, self.driver.earned_money)

    def test__repr__(self):
        result = str(self.driver)
        self.assertEqual(f"{self.driver.name} has {self.driver.miles} miles behind his back.", result)


if __name__ == '__main__':
    main()
