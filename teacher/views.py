from django.http.response import HttpResponseRedirect
from django.shortcuts import get_list_or_404, render
from django.urls import reverse
from django.forms import formset_factory

from management.models import lop_chung
from management.models import hoc_phan
from student.forms import sinhVien_hocPhanForm
from teacher.forms import ChangeDiemForm
from users.models import Teacher, Student
from student.models import lop, sinhvien_hocphan



# Create your views here.
def info(request):
    return HttpResponseRedirect(reverse("home"))


def search_student(request):
    if request.method == "GET":  
        search_text = request.GET.get("q", None)
        records = None
        if search_text:
            records=Student.objects.filter(email__contains=search_text)     
    return render(request, 'teacher/search.html', {
        "records": records
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

def lop_tin_chi_ql(request):
    try:
        lopTinChi = get_list_or_404(lop, teacher=request.user)
    except:
        lopTinChi = None

    return render(request, 'teacher/lopTC_quan_ly.html', {
        'lopTinChi': lopTinChi
    })

def tung_lop_TC(request, lopTC_code):
    lopTC = lop.objects.get(code=lopTC_code)
    
    try: 
        studentTC = lopTC.sinh_vien.all().order_by('code')
    except:
        studentTC = None
    
    data = []

    bangDiemSet = formset_factory(ChangeDiemForm, extra=0)
    for student in studentTC:
        data.append({
            'sinh_vien': student,
            'code': student.code
        })

    bangDiemList = bangDiemSet(request.POST or None, initial=data)

        
    if request.method == "POST":
        bangDiemList = bangDiemSet(request.POST or None, initial=data)
        # for bangDiem in bangDiemList:
        #     bangDiem = ChangeDiemForm(request.POST)
        #     if bangDiem.is_valid():
        #         sinh_vien = bangDiem.cleaned_data['sinh_vien']
        #         code = bangDiem.cleaned_data['code']
        #         giua_ki = bangDiem.cleaned_data['giua_ki']
        #         cuoi_ki = bangDiem.cleaned_data['cuoi_ki']
            
                
                # bd = sinhvien_hocphan.update_or_create()
        return render(request, "teacher/tung_lop_TC.html", {
                "lopTC": lopTC,
                "changeDiemForm": bangDiemList,
                "studentTC": studentTC,
            })   
            
    return render(request, "teacher/tung_lop_TC.html", {
                "lopTC": lopTC,
                "changeDiemForm": bangDiemList,
                "studentTC": studentTC,
            }) 




        
        

    

    




     
    
