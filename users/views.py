from django.http.response import  HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.urls.base import reverse
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .models import User, Teacher, Student
from .forms import loginForm
from django.core import serializers


def login_view(request):
    form = loginForm()
    return render(request, 'user/login.html', {
        'form': form
    })

def login_validate(request):

    if request.is_ajax() and request.method == "POST":
        
        form = loginForm(request.POST)

        login_times = request.session.get('login_times', 0)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return JsonResponse({"data": 'success'}, status=200)
            else:
                request.session['login_times'] = login_times + 1
                return JsonResponse({"data": "fail", "login_times": login_times}, status=200)
        else:
            request.session['login_times'] = login_times + 1
            return JsonResponse({"data": "requied field","login_times": login_times}, status=200)

    return JsonResponse({"error": "Error"}, status=400)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def forget_password(request):
    if request.method == "POST":
        email = request.POST['email']
        try:
            user = User.objects.filter(email=email).first()
        except User.DoesNotExist:
            user = None
        
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
        else:   
            return render(request, 'user/forget_password.html', {
                'message': "Không tìm thấy Email!"
            })

    return render(request, 'user/forget_password.html')
    
    
    