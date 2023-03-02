
from typing import List
from OOP.exercise_inheritance.shop.project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> [Product, None]:
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        final = '\n'.join(f'{prod}: {prod.quantity}' for prod in self.products)
        return ''.join(final)
