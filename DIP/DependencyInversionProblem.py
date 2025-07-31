import smtplib
from email.message import EmailMessage


class Mail:
    def send_mail(self):
        try:
            msg = EmailMessage()
            msg['From'] = 'akshay@dotnetbees.com'
            msg['To'] = 'akshayblevel@gmail.com'
            msg['Subject'] = 'Order Confirmation'
            msg.set_content('Order is placed successfully')

            # Configure SMTP client
            with smtplib.SMTP('smtp.gmail.com', 587) as client:
                client.starttls()
                client.login('akshay@dotnetbees.com', 'your-app-password')  # Use an app-specific password or OAuth2
                client.send_message(msg)
                print("Email sent successfully.")

        except Exception as e:
            raise e


class Order:
    def __init__(self):
        self.mail = Mail()

    def place_order(self):
        try:
            # Place order logic here
            self.mail.send_mail()
        except Exception as ex:
            raise ex


# Example usage
if __name__ == "__main__":
    order = Order()
    order.place_order()