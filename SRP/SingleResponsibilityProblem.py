import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Order:
    def __init__(self):
        pass

    def place_order(self):
        try:
            # Place order logic here
            self.send_email()
        except Exception as ex:
            raise ex
        
    def send_email(self):
        sender_email = "akshay@dotnetbees.com"
        receiver_email = "akshayblevel@gmail.com"
        subject = "Order Confirmation"
        body = "Order is placed successfully"

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server
        try:
            with smtplib.SMTP('smtp.gmail.com', 25) as server:
                server.ehlo()
                server.starttls()
                # server.login(sender_email, "your-password")  # Optional: only if authentication is needed
                server.send_message(msg)
                print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")
            raise

# Example Usage
if __name__ == "__main__":
    order = Order()
    order.place_order()