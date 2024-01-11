from twilio.rest import Client
from keys import *

class NotificationManager: 

    def send_message(self, message):

        client = Client(TWILIO_ACC_SID, TWILIO_AUTH)
        message = client.messages.create(
            from_ = TWILIO_PHONE_NUM,
            body = message,
            to = VERIFIED_NUM
        )

        print(message.sid)