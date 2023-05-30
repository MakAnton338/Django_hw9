from celery import shared_task
from twilio.rest import Client
import keys
import time
#xDgIsuP8YlTHGdvrDCfqQTG3Musbgp1j0g41x-bJ

@shared_task
def twilio_sms():
    client = Client(keys.account_sid, keys_auth_token)
    message = client.messages.create(
        body= "Ola"
        from_key=keys.twilio_number
        to_key=keys.my_phone_number
    )
