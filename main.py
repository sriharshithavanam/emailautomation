#by sri harshitha
import smtplib
import ssl
import csv
from email.message import EmailMessage
import csv
with open('data.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile,delimiter=',')
 for row in data:
    em=EmailMessage()
    email_sender = 'techcrat15@gmail.com'
    email_password = 'hmtt tqvq ztts leke'
    email_reciever=row['Emailid']
    name=row['Name']
    cont_num_in_csv='1234'
    template_text = open('template.txt', 'r').read() # Read Template File
    final_mail_body = template_text.format (name,"9-Jan", cont_num_in_csv)
    em.set_content (final_mail_body)
    # Add SSL (layer of security)
    context = ssl.create_default_context()
    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_reciever, em.as_string())

   