from twilio.rest import Client

def make_reservation_call(to_number, medicine_name):
    account_sid = 'your-twilio-sid'
    auth_token = 'your-twilio-token'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        twiml=f'<Response><Say>A user wants to reserve {medicine_name}. Please confirm.</Say></Response>',
        to=to_number,
        from_='your-twilio-verified-number'
    )
    return call.sid
