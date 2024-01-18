#!/usr/bin/env python
import os
from twilio.rest import Client
from dotenv import load_dotenv
import sqlite3
import time

load_dotenv()


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone = "+18554751750"
receiver_phone = "+14105416242"

client = Client(account_sid, auth_token)

connection = sqlite3.connect("demo.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

rows = cursor.execute("SELECT message from messages").fetchall()
for row in rows:
    print(f'Message: {row["message"]}')

    message = client.messages \
                    .create(
                         body=row["message"],
                         from_=twilio_phone,
                         to=receiver_phone
                     )

    print(message.sid)
    time.sleep(3)

connection.close() 
