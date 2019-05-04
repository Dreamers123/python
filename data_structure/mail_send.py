
import os
import smtplib


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

#contacts = ['YourAddress@gmail.com', 'test@example.com']

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
     smtp.ehlo()
     smtp.starttls()
     smtp.ehlo()

     smtp.login('gotnoname99@gmail.com','mslkhzzvboqqaxcg')

     subject='Grab Dinner'
     body='You can grab it tonight'
     msg= 'Subject:{subject}\n\n{body}'

     smtp.sendmail('gotnoname99@gmail.com','abeerazad19@gmail.com',msg)