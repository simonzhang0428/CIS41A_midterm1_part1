# CIS41A Final
# Author: Simon Zhang
# 06/18/2020
# Burger class, special Burger1,2,3,4,5 extends Burger


class Burger:
    def __init__(self, name=' ', price=0.0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return self.name + str(self.price) + str(self.quantity)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity


class Burger1(Burger):
    def __init__(self):
        super().__init__()
        self.name = 'De Anza Burger'
        self.price = 5.25
        self.quantity = 0


class Burger2(Burger):
    def __init__(self):
        super().__init__()
        self.name = 'Bacon Cheese'
        self.price = 5.75
        self.quantity = 0


class Burger3(Burger):
    def __init__(self):
        super().__init__()
        self.name = 'Mushroom Swiss'
        self.price = 5.95
        self.quantity = 0


class Burger4(Burger):
    def __init__(self):
        super().__init__()
        self.name = 'Western Burger'
        self.price = 5.95
        self.quantity = 0


class Burger5(Burger):
    def __init__(self):
        super().__init__()
        self.name = 'Don Cali Burger'
        self.price = 5.95
        self.quantity = 0
