from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.urls.base import reverse
from users.models import Student
from management.models import lop_chung
from .forms import StudentUpdateForm
from django.views.generic import TemplateView, ListView

# Create your views here.
def student_info(request):
    return HttpResponseRedirect(reverse("home"))


def genaral_class(request):
    student = Student.objects.get(user_ptr=request.user)

    genaralClass = get_object_or_404(lop_chung, pk=student.lop_chung_id)
    studentList = get_list_or_404(Student, lop_chung_id = student.lop_chung_id)
    
    return render(request, "student/genaralClass.html", {
        "studentList": studentList,
        "genaralClass": genaralClass,
    })

def change_info(request):
    student = Student.objects.get(user_ptr=request.user)
    change_form = StudentUpdateForm(instance=student)

    if request.method == "POST":
        print("POST")
        change_form = StudentUpdateForm(request.POST, instance=student)
        if change_form.is_valid():
            change_form.save()
            return HttpResponseRedirect(reverse("student_info"))

    return render(request, "student/change_info.html", {
        "change_form": change_form,
    })
