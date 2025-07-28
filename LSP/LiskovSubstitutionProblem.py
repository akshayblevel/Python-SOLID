from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def deduct_amount(self):
        pass

    @abstractmethod
    def process_transaction(self):
        pass


class Paypal(Payment):
    def check_balance(self):
        print("CheckBalance Method Called")

    def deduct_amount(self):
        print("DeductAmount Method Called")

    def process_transaction(self):
        print("ProcessTransaction Method Called")


class COD(Payment):
    def check_balance(self):
        raise NotImplementedError("CheckBalance not implemented")

    def deduct_amount(self):
        raise NotImplementedError("DeductAmount not implemented")

    def process_transaction(self):
        print("ProcessTransaction Method Called")


# Example usage:
if __name__ == "__main__":
    payment1 = Paypal()
    payment1.check_balance()
    payment1.deduct_amount()
    payment1.process_transaction()

    payment2 = COD()
    try:
        payment2.check_balance()
    except NotImplementedError as e:
        print(e)
    payment2.process_transaction()