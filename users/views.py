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
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email, password)
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return JsonResponse({"data": 'success'}, status=200)
            return JsonResponse({"data": 'fail'}, status=200)
        else:
            return JsonResponse({"data": "requied field"}, status=200)

    return JsonResponse({"error": ""}, status=400)

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
    
    
    # login_form = loginForm(request.POST or None)
    # if request.method == 'POST':
    #     email = request.POST.get('email') 
    #     password = request.POST.get('password') 
    #     user = authenticate(request, email=email, password=password)


    # if request.is_ajax() and request.method == 'POST':
    #     print("1")
    #     email = request.POST.get('email') 
    #     password = request.POST.get('password') 
    #     user = authenticate(request, email=email, password=password)

    #     if user is not None:
    #         login(request, user)
    #         if request.user.role == 0:
    #             student = Student.objects.get(user_ptr=request.user)
    #             return render(request, 'student/info.html', {
    #                     'student': student
    #                 })

    #         else:
    #             teacher = Teacher.objects.get(user_ptr=request.user)
    #             return render(request, 'teacher/info.html', {
    #                 'teacher': teacher
    #             }) 

    #     else:
    #         data['email'] = email
    #         return JsonResponse(data)