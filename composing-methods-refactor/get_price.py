# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# TODO: Replace temporary variable with extracted method/query

# Code snippet. Not runnable.
class Price:
    def __init__(self, quantity, item_price):
        self.quantity = quantity
        self.item_price = item_price
        self.discount_factor = 0
    def get_price(self):
        if self.base_price() > 1000:
            discount_factor = 0.95
        else:
            discount_factor = 0.98
        return self.base_price() * discount_factor

    def base_price(self):
        return self.quantity * self.item_price

price = Price(2, 13)
