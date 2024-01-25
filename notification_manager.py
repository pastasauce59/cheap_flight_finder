from twilio.rest import Client
import smtplib
from keys import *

class NotificationManager: 

    def send_sms(self, message):

        client = Client(TWILIO_ACC_SID, TWILIO_AUTH)
        message = client.messages.create(
            from_ = TWILIO_PHONE_NUM,
            body = message,
            to = VERIFIED_NUM
        )

        print(message.status)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:NEW LOW PRICE! \n\n{message}".encode('utf-8')
                )