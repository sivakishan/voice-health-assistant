import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

def make_reservation_call(to_number, medicine_name):
    account_sid = 'ACee661d696689f319bc0eb22d0f8a6cfb'
    auth_token = 'e3cc53e447d4c1f7eceb979feec38ea8'
    from_number = os.getenv('+13608432103')

    client = Client(account_sid, auth_token)
    call = client.calls.create(
        twiml=f'<Response><Say>A user wants to reserve {medicine_name}. Please confirm.</Say></Response>',
        to=to_number,
        from_=from_number
    )
    return call.sid
