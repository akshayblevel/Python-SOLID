from Checkout import Checkout


class Amazon(Checkout):
    def calculate_shipping_cost(self, order_amount):
        return order_amount + (order_amount * 0.05)