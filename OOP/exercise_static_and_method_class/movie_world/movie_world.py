from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        cust_age = 0
        age_rest = 0
        customer_name = ''
        for customer in self.customers:
            if customer.id == customer_id:
                cust_age = customer.age
                customer_name = customer.name
                for d in customer.rented_dvds:
                    if d.id == dvd_id:
                        return f'{customer.name} has already rented {d.name}'

        for dvds in self.dvds:
            if dvds.id == dvd_id:
                age_rest = dvds.age_restriction
                if dvds.is_rented:
                    return "DVD is already rented"

        if cust_age < age_rest:
            return f'{customer_name} should be at least {age_rest} to rent this movie'

        for customer in self.customers:
            if customer_id == customer.id:
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = True
                        customer.rented_dvds.append(dvd)
                        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        customer_name = ''
        for customer in self.customers:
            if customer.id == customer_id:
                customer_name = customer.name
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = False
                        customer.rented_dvds.remove(dvd)
                        return f'{customer.name} has successfully returned {dvd.name}'
        return f'{customer_name} does not have that DVD'

    def __repr__(self):
        customers = '\n'.join(str(cust) for cust in self.customers)
        dvds = '\n'.join(str(dvd) for dvd in self.dvds)
        return f'{customers}\n{dvds}'
