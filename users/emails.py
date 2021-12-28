from django.template.loader import render_to_string
from django.urls.base import reverse
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
import os

from university_management.settings import BASE_DIR

def send_raw_password(user, password):

    massage_template = 'user\send_raw_password_to_user.txt' 
    context = {
            "password": password,
            "email":user.email,
            'domain':'127.0.0.1:8000',
            'site_name': 'Website',
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "user": user,
            'token': default_token_generator.make_token(user),
            'protocol': 'http',
            }
    email_message = render_to_string(massage_template, context)
    send_mail(
        'Password Reset Request',
        email_message,
        'admin@gmail.com',
        [user.email],
        fail_silently=False
    )

def save_raw_password(user ,password):
    path = os.path.join(BASE_DIR, 'raw_password.txt')
    with open(path, 'a') as f:
        f.write(f"{user.email}: {password} \n")
    



            

    