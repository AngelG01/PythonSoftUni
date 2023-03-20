from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in [d.name for d in self.delicacies]:
            raise Exception(f"{name} already exists!")

        if type_delicacy == 'Gingerbread':
            curr_product = Gingerbread(name, price)
        elif type_delicacy == 'Stolen':
            curr_product = Stolen(name, price)
        else:
            raise Exception(f'{type_delicacy} is not on our delicacy menu!')

        self.delicacies.append(curr_product)
        return f'Added delicacy {name} - {type_delicacy} to the pastry shop.'

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f'Booth number {booth_number} already exists!')

        if type_booth == 'Open Booth':
            curr_booth = OpenBooth(booth_number, capacity)
        elif type_booth == 'Private Booth':
            curr_booth = PrivateBooth(booth_number, capacity)
        else:
            raise Exception(f'{type_booth} is not a valid booth!')

        self.booths.append(curr_booth)
        return f'Added booth number {booth_number} in the pastry shop.'

    def reserve_booth(self, number_of_people: int):
        for b in self.booths:
            if number_of_people <= b.capacity and not b.is_reserved:
                b.reserve(number_of_people)
                return f'Booth {b.booth_number} has been reserved for {number_of_people} people.'

        raise Exception(f'No available booth for {number_of_people} people!')

    def order_delicacy(self, booth_number: int, delicacy_name: str):

        if booth_number not in [b.booth_number for b in self.booths]:
            raise Exception(f'Could not find booth {booth_number}!')

        if delicacy_name not in [d.name for d in self.delicacies]:
            raise Exception(f'No {delicacy_name} in the pastry shop!')

        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        dish = [d for d in self.delicacies if d.name == delicacy_name][0]

        booth.delicacy_order.append(dish)
        return f'Booth {booth_number} ordered {delicacy_name}.'

    def leave_booth(self, booth_number: int):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                total = booth.price_for_reservation
                food_total = sum(d.price for d in booth.delicacy_order)
                final_cost = total + food_total

                self.income += final_cost

                booth.delicacy_order = []
                booth.is_reserved = False
                booth.price_for_reservation = 0

                return f'Booth {booth_number}:\nBill: {final_cost:.2f}lv.'

    def get_income(self):
        return f'Income: {self.income:.2f}lv.'
