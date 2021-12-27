from django.http.response import HttpResponseRedirect
from django.shortcuts import get_list_or_404, render, get_object_or_404
from management.models import lop_chung
from users.models import Student
from django.urls import reverse
from student.models import lop
from django.http import JsonResponse



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
    lopChungname = ten_lop_chung.split("_")[0]
    lopChungkhoa = ten_lop_chung.split("_")[1]
    lopChung = lop_chung.objects.select_related('khoa').get(name=lopChungname, khoa__name=lopChungkhoa)
    try: 
        studentList = Student.objects.filter(lop_chung=lopChung).order_by('code')
    except:
        studentList = None
    return render(request, 'teacher/tung_lop_chung.html', {
        'lopChung': lopChung,
        'studentList': studentList
    })

def search_student(request):
    if request.method == "GET":  
        search_text = request.GET.get("q", None)
        records = None
        if search_text:
            records=Student.objects.filter(email__contains=search_text)     
    return render(request, 'teacher/search.html', {
        "records": records
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