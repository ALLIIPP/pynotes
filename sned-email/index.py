#!/usr/bin/python3

import smtplib

sender = ""
receiver = ""
password = ""
subject = ""
body = ""

#header 
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""


server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
try:
    server.login()
    print('logged in...')
except Exception as e:
    print('Login Failed : {}'.format(e))

server.sendmail(sender,receiver,message)
print('Email has been sent')