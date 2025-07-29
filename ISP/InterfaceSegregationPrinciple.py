from abc import ABC, abstractmethod

# IShippingCost interface
class IShippingCost(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

# IOrder interface
class IOrder(ABC):
    @abstractmethod
    def process_payment(self):
        pass

    @abstractmethod
    def place_order(self):
        pass

# StorePickupOrder implements IOrder
class StorePickupOrder(IOrder):
    def place_order(self):
        print("PlaceOrder Method is Called")

    def process_payment(self):
        print("ProcessPayment Method is Called")

# HomeDeliveryOrder implements both IShippingCost and IOrder
class HomeDeliveryOrder(IShippingCost, IOrder):
    def calculate_shipping_cost(self):
        print("CalculateShippingCost Method is Called")

    def place_order(self):
        print("PlaceOrder Method is Called")

    def process_payment(self):
        print("ProcessPayment Method is Called")


# Example usage
if __name__ == "__main__":
    store_order = StorePickupOrder()
    store_order.process_payment()
    store_order.place_order()

    print("---")

    home_order = HomeDeliveryOrder()
    home_order.calculate_shipping_cost()
    home_order.process_payment()
    home_order.place_order()