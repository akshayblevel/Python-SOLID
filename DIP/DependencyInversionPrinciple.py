from abc import ABC, abstractmethod
import smtplib
from email.message import EmailMessage


# IMail interface
class IMail(ABC):
    @abstractmethod
    def send_mail(self):
        pass


# Mail class implementing IMail
class Mail(IMail):
    def send_mail(self):
        try:
            msg = EmailMessage()
            msg['From'] = 'akshay@dotnetbees.com'
            msg['To'] = 'akshayblevel@gmail.com'
            msg['Subject'] = 'Order Confirmation'
            msg.set_content('Order is placed successfully')

            with smtplib.SMTP('smtp.gmail.com', 587) as client:
                client.starttls()
                client.login('akshay@dotnetbees.com', 'your-app-password')  # Replace with a secure method
                client.send_message(msg)
                print("Email sent successfully.")

        except Exception as e:
            raise e


# Order class with dependency injection
class Order:
    def __init__(self, mail: IMail):
        self.mail = mail

    def place_order(self):
        try:
            # Place order logic goes here
            self.mail.send_mail()
        except Exception as ex:
            raise ex


# Example usage
if __name__ == "__main__":
    mail_service = Mail()
    order = Order(mail_service)
    order.place_order()