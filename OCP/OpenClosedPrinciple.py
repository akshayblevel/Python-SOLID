class Checkout:
    def __init__(self):
        self._merchant = None  # private-like variable (by convention)

    @property
    def merchant(self):
        return self._merchant

    @merchant.setter
    def merchant(self, value):
        self._merchant = value

    def calculate_shipping_cost(self, order_amount):
        shipping_cost = 0
        if self._merchant == "Flipkart":
            shipping_cost = order_amount + (order_amount * 0.10)
        elif self._merchant == "Amazon":
            shipping_cost = order_amount + (order_amount * 0.05)
        # else: leave as 0
        return shipping_cost