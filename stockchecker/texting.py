import os
from twilio.rest import Client


account_sid = 'YOURTWILIOACCOUNT'
auth_token = 'YOURTWILIOAUTH'
client = Client(account_sid, auth_token)

def send_text(store):
    client.messages \
        .create(
        body=f"There may be a PS5 in stock at {store}",
        from_='YOURTWILIOPHONENUMBER',
        to='YOURPHONENUMBER'
    )

