from Amazon import Amazon
from Flipkart import Flipkart


def main():
    order_amount = 1000

    flipkart_checkout = Flipkart()
    amazon_checkout = Amazon()

    print("Flipkart Shipping Cost:", flipkart_checkout.calculate_shipping_cost(order_amount))
    print("Amazon Shipping Cost:", amazon_checkout.calculate_shipping_cost(order_amount))


if __name__ == "__main__":
    main()