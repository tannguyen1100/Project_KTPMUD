from django.shortcuts import render
from django.urls.base import reverse
from django.contrib.auth import logout
from users.models import Student, Teacher


def home(request):
    if request.user.is_superuser:
        logout(request)
    
    if request.user.is_authenticated:
        if request.user.role == 0:
            student = Student.objects.get(user_ptr=request.user)
            return render(request, 'student/info.html', {
                    'student': student
                })

        if request.user.role == 1:
            teacher = Teacher.objects.get(user_ptr=request.user)
            return render(request, 'teacher/info.html', {
                'teacher': teacher,
            }) 

    return render(request, 'home.html')