from abc import ABC, abstractmethod

# Define the IOrder interface
class IOrder(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

    @abstractmethod
    def process_payment(self):
        pass

    @abstractmethod
    def place_order(self):
        pass

# StorePickupOrder implements IOrder
class StorePickupOrder(IOrder):
    def calculate_shipping_cost(self):
        raise NotImplementedError("CalculateShippingCost not implemented")

    def process_payment(self):
        print("ProcessPayment Method is Called")

    def place_order(self):
        print("PlaceOrder Method is Called")

# HomeDeliveryOrder implements IOrder
class HomeDeliveryOrder(IOrder):
    def calculate_shipping_cost(self):
        print("CalculateShippingCost Method is Called")

    def process_payment(self):
        print("ProcessPayment Method is Called")

    def place_order(self):
        print("PlaceOrder Method is Called")


# Example usage
if __name__ == "__main__":
    order1 = StorePickupOrder()
    try:
        order1.calculate_shipping_cost()
    except NotImplementedError as e:
        print(e)
    order1.process_payment()
    order1.place_order()

    print("---")

    order2 = HomeDeliveryOrder()
    order2.calculate_shipping_cost()
    order2.process_payment()
    order2.place_order()