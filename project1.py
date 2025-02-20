import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    sender = "jeevijeevithalgowda31@gmail.com"
    receiver = "yashasgowdamb28@gmail.com"
    msg = MIMEText(message)
    msg['Subject'] = 'Alert!'
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.login(sender, 'jeevi123')
        server.sendmail(sender, receiver, msg.as_string())