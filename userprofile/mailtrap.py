import os
import smtplib
from email.mime.text import MIMEText


def send_mail(subject, body, from_email, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # The actual mail send
    server = smtplib.SMTP('mailtrap.io', 2525)
    server.starttls()
    server.login(os.environ['EMAIL_USER'], os.environ['EMAIL_PASS'])
    server.sendmail( from_email, [to_email], msg.as_string())
    server.quit()
