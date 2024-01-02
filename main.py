import smtplib
import datetime as dt
import random
now=dt.datetime.now()
weekday=now.weekday()

#Will send a mail only on Mondays
if weekday==0:
    with open("quotes.txt") as file:
        quotes=file.readlines()
    random_quote=random.choice(quotes)


    my_email="YOUR EMAIL HERE"
    #Refer the link on how to generate an app password https://www.youtube.com/watch?v=hXiPshHn9Pw
    password="YOUR APP PASSWORD HERE"
    
    #Gmail: smtp.gmail.com , Hotmail: smtp.live.com, Outlook: outlook.office365.com, Yahoo: smtp.mail.yahoo.com
    smtp_address="SMTP ADDRESS AS ABOVE"

    with smtplib.SMTP(smtp_address) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="Receiver mail",msg=f"Subject:Monday Motivation\n\n{random_quote}")