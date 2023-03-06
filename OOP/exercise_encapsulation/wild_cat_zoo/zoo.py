class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price: int):
        if len(self.animals) < self.__animal_capacity and price <= self.__budget:
            self.animals.append(animal)
            self.__budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        elif len(self.animals) <= self.__animal_capacity and price > self.__budget:
            return 'Not enough budget'
        elif len(self.animals) >= self.__animal_capacity and price <= self.__budget:
            return 'Not enough space for animal'

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        else:
            return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_pays = 0
        for worker in self.workers:
            total_pays += worker.salary

        if total_pays >= self.__budget:
            return f'You have no budget to pay your workers. They are unhappy'

        self.__budget -= total_pays
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        total_care_needed = 0
        for animal in self.animals:
            total_care_needed += animal.money_for_care

        if total_care_needed >= self.__budget:
            return 'You have no budget to tend the animals. They are unhappy.'
        self.__budget -= total_care_needed
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        animals_dict = {'Lions': [], 'Tigers': [], 'Cheetahs': []}

        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                animals_dict['Lions'].append(animal)
            elif animal.__class__.__name__ == 'Tiger':
                animals_dict['Tigers'].append(animal)
            elif animal.__class__.__name__ == 'Cheetah':
                animals_dict['Cheetahs'].append(animal)
        lions = "\n".join(str(x) for x in animals_dict["Lions"])
        tigers = "\n".join(str(x) for x in animals_dict["Tigers"])
        cheetahs = "\n".join(str(x) for x in animals_dict["Cheetahs"])
        final = f'You have {len(self.animals)} animals' + \
                f'\n----- {len(animals_dict["Lions"])} Lions:\n{"".join(lions)}' \
                f'\n----- {len(animals_dict["Tigers"])} Tigers:\n{"".join(tigers)}' \
                f'\n----- {len(animals_dict["Cheetahs"])} Cheetahs:\n{"".join(cheetahs)}'
        return final

    def workers_status(self):
        workers_dict = {'Keeper': [], 'Caretaker': [], 'Vet': []}

        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                workers_dict['Keeper'].append(worker)
            elif worker.__class__.__name__ == 'Caretaker':
                workers_dict['Caretaker'].append(worker)
            elif worker.__class__.__name__ == 'Vet':
                workers_dict['Vet'].append(worker)
        keepers = "\n".join(str(x) for x in workers_dict['Keeper'])
        caretakers = "\n".join(str(x) for x in workers_dict['Caretaker'])
        vet = "\n".join(str(x) for x in workers_dict['Vet'])

        final = f'You have {len(self.workers)} workers' + \
                f'\n----- {len(workers_dict["Keeper"])} Keepers:\n{"".join(keepers)}' \
                f'\n----- {len(workers_dict["Caretaker"])} Caretakers:\n{"".join(caretakers)}' \
                f'\n----- {len(workers_dict["Vet"])} Vets:\n{"".join(vet)}'

        return final
