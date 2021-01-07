from twilio.rest import Client
import requests
import smtplib
import config
TWILIO_SID = config.TWILIO_SID
TWILIO_AUTH_TOKEN = config.TWILIO_AUTH_TOKEN
TWILIO_VIRTUAL_NUMBER = config.TWILIO_VIRTUAL_NUMBER
TWILIO_VERIFIED_NUMBER = config.TWILIO_VERIFIED_NUMBER

my_email = config.my_email
my_password = config.my_password

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, message, user_list):

        for user in user_list:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email, to_addrs=user["email"],
                                    msg=f"subject:Low flight deals!\n\nHey {user['firstName']}!\n{message}".encode('utf-8'))


