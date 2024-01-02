import smtplib
import datetime as dt
import random
now=dt.datetime.now()
weekday=now.weekday()

if weekday==0:
    with open("quotes.txt") as file:
        quotes=file.readlines()
    random_quote=random.choice(quotes)
    print(random_quote)