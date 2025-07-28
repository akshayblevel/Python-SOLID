from abc import ABC, abstractmethod

# Abstract base class simulating the abstract class Payment
class Payment(ABC):
    @abstractmethod
    def process_transaction(self):
        pass

# Interface-like structure using ABC
class IPayment(ABC):
    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def deduct_amount(self):
        pass

# Paypal implements both Payment and IPayment
class Paypal(Payment, IPayment):
    def check_balance(self):
        print("CheckBalance Method Called")

    def deduct_amount(self):
        print("DeductAmount Method Called")

    def process_transaction(self):
        print("ProcessTransaction Method Called For Paypal")

# COD only implements Payment
class COD(Payment):
    def process_transaction(self):
        print("ProcessTransaction Method Called For COD")


# Example usage
if __name__ == "__main__":
    paypal = Paypal()
    paypal.check_balance()
    paypal.deduct_amount()
    paypal.process_transaction()

    cod = COD()
    cod.process_transaction()