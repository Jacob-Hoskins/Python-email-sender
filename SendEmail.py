import smtplib
import ssl
from email.message import EmailMessage

context = ssl.create_default_context()

def auth(username, password):
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(username, password)
            return True

    except:
        return False

def sendMessage(sender, receiver, subject, content, password):
    message = EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())

