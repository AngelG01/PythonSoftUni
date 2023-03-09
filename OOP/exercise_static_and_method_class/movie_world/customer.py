class Customer:
    def __init__(self, name: str, age: int, identification_number: int):
        self.name = name
        self.age = age
        self.id = identification_number
        self.rented_dvds = []

    def __repr__(self):
        dvds_rented = ', '.join(dvd.name for dvd in self.rented_dvds)
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's " \
               f"({dvds_rented})"
