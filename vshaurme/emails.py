from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from vshaurme.extensions import mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

def send_mail(to, subject, template, **kwargs):
    message = Mail(
        from_email='devman305@gmail.com',
        to_emails=to,
        subject=subject,
        html_content=render_template(template, **kwargs))
    try:
        sg = SendGridAPIClient(os.getenv('sendgridapi'))
        response = sg.send(message)
        #print(response.status_code)
        #print(response.body)
        #print(response.headers)
    except Exception as e:
        print(e)


def send_confirm_email(user, token, to=None):
    token = token.decode("utf-8")
    send_mail(subject='Подтверждение адреса почты/Email Confirm', to=to or user.email, template='emails/confirm.html', user=user, token=token)


def send_reset_password_email(user, token):
    send_mail(subject='Сброс пароля/Password Reset', to=user.email, template='emails/reset_password.html', user=user, token=token)


def send_change_email_email(user, token, to=None):
    send_mail(subject='Подтверждение смены адреса почты/Смена Change Email Confirm', to=to or user.email, template='emails/change_email.html', user=user, token=token)
