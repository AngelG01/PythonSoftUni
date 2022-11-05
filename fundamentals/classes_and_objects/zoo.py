class Zoo:
    __animals = 0

    def __init__(self, name_of_the_zoo):
        self.name_of_the_zoo = name_of_the_zoo
        self.mammals = []
        self.birds = []
        self.fishes = []

    def add_animals(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ''

        if species == 'mammal':
            result += f'Mammals in {self.name_of_the_zoo}: {", ".join(self.mammals)}\n'
        elif species == 'bird':
            result += f'Birds in {self.name_of_the_zoo}: {", ".join(self.birds)}\n'
        else:
            result += f'Fishes in {self.name_of_the_zoo}: {", ".join(self.fishes)}\n'
        result += f'Total animals: {self.__animals}'
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for i in range(count):
    animal = input().split()
    species = animal[0]
    name = animal[1]

    zoo.add_animals(species, name)

info = input()
print(zoo.get_info(info))
