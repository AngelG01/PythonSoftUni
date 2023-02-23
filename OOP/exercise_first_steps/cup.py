class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, amount):
        new_q = self.quantity + amount

        if new_q <= self.size:
            self.quantity = new_q

    def status(self):
        return self.size - self.quantity

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())