from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
def send_mail(mail,text):
    try:
        msg = MIMEMultipart()# create message object instance
        message=text
        # setup the parameters of the message
        password = "p232kv20"
        msg['From'] = "u-p.91@mail.ru"
        msg['To'] = mail
        msg['Subject'] = "Subscription"
        msg.attach(MIMEText(message, 'plain'))# add in the message body
        server = smtplib.SMTP('smtp.mail.ru')#create server
        server.starttls()
        server.login(msg['From'], password)# Login Credentials for sending the mail
        server.send_message(msg)# send the message via the server.
        server.quit()
        print("successfully sent email to %s:"%(msg['To']))
    except TimeoutError as e:
        print("Message not delivered")
        print(e)
