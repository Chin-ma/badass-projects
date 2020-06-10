from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import re

def email_with_attachments(sender_email,sender_password,receiver_email,subject,body,html_present,attachment,attachment_location):
    email = MIMEMultipart()
    email['From'] = sender_email
    email['To'] = receiver_email
    email['Subject'] = subject
    if html_present:
        link_format = re.compile(r"<a href=.+>.+</a>")
        link = link_format.search(body).group()
        new_text = link_format.sub('', body)
        email.attach(MIMEText(new_text, 'plain'))
        email.attach(MIMEText(link, 'html'))
    else:
        email.attach(MIMEText(body, 'plain'))


    new = MIMEBase('application', 'octet-stream')
    to_attach = open(attachment_location, 'rb')
    new.set_payload(to_attach.read())
    encoders.encode_base64(new)
    new.add_header('Content-Disposition', f'attachment; filename={attachment}')
    email.attach(new)

    session = SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_email, sender_password)
    session.sendmail(sender_email, receiver_email, email.as_string())
    session.quit()

def email_without_attachments(sender_email,sender_password,receiver_email,subject,body, html_present):
    email = MIMEMultipart()
    email['From'] = sender_email
    email['To'] = receiver_email
    email['Subject'] = subject
    if html_present:
        link_format = re.compile(r"<a href=.+>.+</a>")
        link = link_format.search(body).group()
        new_text = link_format.sub('', body)
        email.attach(MIMEText(new_text, 'plain'))
        email.attach(MIMEText(link, 'html'))
    else:
        email.attach(MIMEText(body, 'plain'))

    session = SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_email, sender_password)
    session.sendmail(sender_email, receiver_email, email.as_string())
    session.quit()








