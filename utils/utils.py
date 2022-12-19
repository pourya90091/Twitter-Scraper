from django.http import Http404
from utils.enigma.enigma_code_decode import code as encode, rotors_config as true_rotors_config
from django.conf import settings
import re

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def access_check(function_view):
    def wrapper(req, *args, **kwargs):
        if 'Cookie' in req.headers:
            code = re.findall(r'access_token=(.+)', req.headers['Cookie'])
            if code:
                code = code[0]
                try:
                    true_code = encode(settings.SECRET, true_rotors_config)
                    if code != true_code:
                        raise Exception()
                except Exception:
                    raise Http404()
                else:
                    return function_view(req, *args, **kwargs)
        raise Http404()
    return wrapper


def send_email(sender, getter, password, subject, message):
    print(f'sender : {sender}\ngetter : {getter}')

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = getter
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, getter, msg.as_string())
        server.quit()

        print(f'email sent from {sender} to {getter}')
    except Exception as err:
        raise Exception(err)
