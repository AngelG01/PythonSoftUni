class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTest(unittest.TestCase):

    def test_initialization(self):
        worker = Worker('Ivan Ivanov', 1000, 10)
        self.assertEqual(worker.name, 'Ivan Ivanov')
        self.assertEqual(worker.salary, 1000)
        self.assertEqual(worker.energy, 10)

    def test_rest(self):
        worker = Worker('Ivan Ivanov', 1000, 10)
        worker.rest()
        self.assertEqual(worker.energy, 11)

    def test_is_energy_negative(self):
        worker = Worker('Ivan Ivanov', 1000, -1)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_is_energy_zero(self):
        worker = Worker('Ivan Ivanov', 1000, 0)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_salary_check(self):
        worker = Worker('Ivan Ivanov', 1000, 10)
        worker.work()
        self.assertEqual(worker.money, worker.salary)

    def test_working_energy(self):
        worker = Worker('Ivan Ivanov', 1000, 10)
        worker.work()
        self.assertEqual(worker.energy, 9)

    def test_get_info(self):
        worker = Worker('Ivan Ivanov', 1000, 10)
        self.assertEqual(worker.get_info(), f'{worker.name} has saved {worker.money} money.')


if __name__ == '__main__':
    unittest.main()
