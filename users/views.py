from django.http.response import  HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from users.models import User
from django.urls.base import reverse
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


def login_view(request):
    if (request.method == 'POST'):
        email = request.POST.get('email') #Get email value from form
        password = request.POST.get('password') #Get password value from form
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_authenticated:
                return HttpResponseRedirect(reverse("home"))
             
        else:
            return render(request, "user/login.html", {
                "message": "Invalid credentials."
            })
    return render(request, 'user/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def forget_password(request):
    if request.method == "POST":
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
        except:
            return render(request, 'user/forget_password.html', {
                'message': "Email not found"
            })
        if user:
            massage_template = 'user\password_reset_email.txt' 
            context = {
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
    
            return render(request, "home.html", {
                "message": "Success sending reset password"
            })
            

    return render(request, 'user/forget_password.html')
    
    
