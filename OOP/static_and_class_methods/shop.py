class Shop:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, type: str):
        return cls(name, type, 10)

    def add_item(self, item_name: str):
        curr_cap = 0
        for i, v in self.items.items():
            curr_cap += v

        if curr_cap >= self.capacity:
            return f'Not enough capacity in the shop'

        if item_name in self.items.keys():
            self.items[item_name] += 1
        else:
            self.items[item_name] = 1
        return f'{item_name} added to the shop'

    def remove_item(self, item_name: str, amount: int):
        if item_name not in self.items.keys():
            return f'Cannot remove {amount} {item_name}'

        if amount <= self.items[item_name]:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]

            return f'{amount} {item_name} removed from the shop'
        return f'Cannot remove {amount} {item_name}'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'

