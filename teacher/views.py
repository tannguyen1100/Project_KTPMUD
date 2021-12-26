from django.http.response import HttpResponseRedirect
from django.shortcuts import get_list_or_404, render, get_object_or_404
from management.models import lop_chung
from users.models import Student
from django.urls import reverse
from student.models import lop


# Create your views here.
def info(request):
    return HttpResponseRedirect(reverse("home"))

def lop_chung_quan_ly(request):
    try: 
        lop_chung_quan_ly = get_list_or_404(lop_chung, giao_vien=request.user)
    except:
        lop_chung_quan_ly = None

    return render(request, 'teacher/lop_chung_quan_ly.html', {
        'lop_chung_quan_ly': lop_chung_quan_ly,
    })

def tung_lop_chung(request, ten_lop_chung):
    lopChung = lop_chung.objects.get(name=ten_lop_chung)
    try: 
        studentList = get_list_or_404(Student, lop_chung_id=lopChung.id)
    except:
        studentList = None
    return render(request, 'teacher/tung_lop_chung.html', {
        'lopChung': lopChung,
        'studentList': studentList
    })

def lop_tin_chi_ql(request):
    try:
        lopTinChi = get_list_or_404(lop, teacher=request.user)
    except:
        lopTinChi = None

    return render(request, 'teacher/lopTC_quan_ly.html', {
        'lopTinChi': lopTinChi
    })
     
    
def info_student(request, student_code):
    try:
        sv = Student.objects.get(code=student_code)
    except:
        sv = None

    return render(request, 'student/info.html', {
        'student': sv,
        'input_code': student_code,
    })