import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:
    @staticmethod
    def send_mail():
        sender_email = "akshay@dotnetbees.com"
        receiver_email = "akshayblevel@gmail.com"
        subject = "Order Confirmation"
        body = "Order is placed successfully"

        # Create MIME message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP('smtp.gmail.com', 25) as server:
                server.ehlo()
                server.starttls()  # Secure the connection
                # server.login(sender_email, "your-password")  # Optional authentication
                server.send_message(msg)
                print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")
            raise


# Example usage:
if __name__ == "__main__":
    Mail.send_mail()