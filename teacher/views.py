from email import message
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_list_or_404, render
from django.urls import reverse
from django.forms import formset_factory
from django.db.models import Q

from management.models import lop_chung, semester
from teacher.forms import ChangeDiemForm, DoAnForm
from users.models import Teacher, Student
from student.models import lop_tin_chi_detail, sinhVien_lopTinChiDetail
from teacher.models import do_an



# Create your views here.
def info(request):
    return HttpResponseRedirect(reverse("home"))

def search(request):
    return render(request, 'teacher/search-ajax.html', {
    })

def search_student_ajax(request):
    if request.is_ajax():
        students = request.POST.get('student')
        qs = Student.objects.filter(Q(email__icontains=students) | Q(code__icontains=students) | Q(firstname__icontains=students) | Q(surname__icontains=students) | Q(lastname__icontains=students))
        if len(qs) > 0 and len(students) > 0:
            data = []
            for student in qs:
                item = {
                    'email': student.email,
                    'code': student.code,
                    'name': student.name_with_code()
                }
                data.append(item)
            response = data
        else:
            response = "No Student found ..."

        return JsonResponse({'data': response})
    return JsonResponse({})


def search_student(request):
    if request.method == "GET":  
        search_text = request.GET.get("q", None)
        students = None
        if search_text:
            students=Student.objects.filter(email__contains=search_text)     
    return render(request, 'teacher/search.html', {
        "students": students
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
        lopTinChiDetail_objects = get_list_or_404(lop_tin_chi_detail, teacher=request.user)
    except:
        lopTinChiDetail_objects = None

    return render(request, 'teacher/lopTC_quan_ly.html', {
        'lopTinChiDetail_objects': lopTinChiDetail_objects
    })

def tung_lop_TC(request, sem , lopTC_code):
    semester_object = semester.objects.get(name=sem)
    lopTC_info = None
    try:
        bangDiem_object = sinhVien_lopTinChiDetail.objects.filter(lopTinChiDetail__lopTinChi__code=lopTC_code, lopTinChiDetail__semester=semester_object)
        lopTC_info = bangDiem_object[0].lopTinChiDetail
    
    

        data = []

        bangDiemSet = formset_factory(ChangeDiemForm, extra=0)
        for bangDiem in bangDiem_object:
            data.append({
                'sinh_vien': bangDiem.sinhVien.getfullname(),
                'code': bangDiem.sinhVien.code,
                'giua_ki': bangDiem.giua_ki,
                'cuoi_ki': bangDiem.cuoi_ki,
            })

        bangDiemList = bangDiemSet(request.POST or None, initial=data)

            
        if request.method == "POST":
            bangDiemList = bangDiemSet(request.POST or None, initial=data)
            for bangDiem in bangDiemList:
                if bangDiem.is_valid():
                    code = bangDiem.cleaned_data['code']
                    giua_ki = bangDiem.cleaned_data['giua_ki']
                    cuoi_ki = bangDiem.cleaned_data['cuoi_ki']
                    updated_values = {'giua_ki': giua_ki, 'cuoi_ki': cuoi_ki}
                    student_instance = Student.objects.get(code=code)
                    sinhVien_lopTinChiDetail.objects.update_or_create(sinhVien=student_instance,lopTinChiDetail__lopTinChi__code=lopTC_code, lopTinChiDetail__semester=semester_object, defaults=updated_values)
                
            return render(request, "teacher/tung_lop_TC.html", {
                    "changeDiemForm": bangDiemList,
                    "lopInfo": lopTC_info,
                })   

    except:
        bangDiem_object = None
        return render(request, "teacher/tung_lop_TC.html", {
                "message": "Not found"
            }) 

            
    return render(request, "teacher/tung_lop_TC.html", {
                "changeDiemForm": bangDiemList,
                "lopInfo": lopTC_info,
            }) 

def do_an_view(request):
    teacher = Teacher.objects.get(user_ptr= request.user)
    do_an_list = teacher.do_an_tham_gia.all().order_by('name')

    return render(request, 'teacher/do_an.html', {
        "do_an_list": do_an_list,
    })

def tung_do_an(request, slug_name):
    doAnData = {}
    doAn = do_an.objects.get(slug_name=slug_name)

    student_init = ""
    for student in doAn.student.all():
        student_init = student_init + student.name_with_code() + ", "
    student_init=student_init.strip()[:-1]
    

    teacher_init = ""
    for teacher in doAn.teacher.all():
        teacher_init = teacher_init + teacher.__str__() + ","
    teacher_init=teacher_init[:-1]

    doAnData = {
        'name': doAn.name,
        'slug_name': doAn.slug_name,
        'start_time': doAn.start_time,
        'end_time': doAn.end_time,
        'sinh_vien': student_init,
        'giao_vien': teacher_init,
    }

    for key, value in doAnData.items():
        if value == None:
            doAnData[key] = ""


    form = DoAnForm(request.POST or None, initial=doAnData)

    if request.method == "POST":
        form = DoAnForm(request.POST or None, initial=doAnData)
        if form.is_valid():
            print(1)
            form.save()
            return render(request, 'teacher/tung_do_an.html', {
                'do_an': doAn,
                'form': form,
            })
        else:
            print()
            return render(request, 'teacher/tung_do_an.html', {
                'do_an': doAn,
                'form': form,
            })

    return render(request, 'teacher/tung_do_an.html', {
        'do_an': doAn,
        'form': form,
    })

def them_do_an(request):
    teacher = Teacher.objects.get(user_ptr= request.user)
    form = DoAnForm(request.POST or None)
    if request.method ==  "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("do_an"))
        else:
            message = form.errors
            print(message)
            return render(request, 'teacher/them_do_an.html', {
                'form': form,
                'message': message,
            })

    return render(request, 'teacher/them_do_an.html', {
        'form': form,
    })



        
        

    

    




     
    
