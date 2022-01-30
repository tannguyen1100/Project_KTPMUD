from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.urls.base import reverse
from student.models import lop_tin_chi_detail, sinhVien_lopTinChiDetail
from users.models import Student
from management.models import lop_chung, semester
from .forms import StudentUpdateForm

 
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

def lopTC_trong_ki(request):
    semester_object = semester.objects.get(is_active=True)
    lopTinChitrongKi = lop_tin_chi_detail.objects.filter(semester=semester_object).order_by('lopTinChi__code')

    return render(request, 'student/lopTC_trong_ki.html', {
        "lopTinChitrongKi": lopTinChitrongKi,
    })


def add_lopTinChi_ajax(request):
    active_semester = semester.objects.get(is_active=True)
    if request.is_ajax():
        lopTinChi = request.POST.get('lopTinChi')
        if len(lopTinChi) != 6:
            response = "Invalid" 
            return JsonResponse({'data': response})
        else:
            try:
                lopTC_object = lop_tin_chi_detail.objects.get(lopTinChi__code=lopTinChi,semester=active_semester )
            except lop_tin_chi_detail.DoesNotExist:
                lopTC_object = None
                return JsonResponse({'data': "Invalid"})

            data = {
                'code': lopTC_object.lopTinChi.code,
                'hocPhan': lopTC_object.lopTinChi.hocPhan.name,
                'teacher': lopTC_object.teacher.getfullname(),
                'thoiGian': lopTC_object.timing.__str__(),
                'day': lopTC_object.timetable.day,
                'week': lopTC_object.timetable.display_week(),
            }
            response = data

            return JsonResponse({'data': response})
    return JsonResponse({})


def dang_ki_hoc_tap(request):
    if request.method == "POST":    
        lopDangKi = request.POST.getlist('lopTinChiCode')
        deletions = request.POST.items()
        print(lopDangKi)
        for key, value in deletions:
            print(key)
            print(value)

    return render(request, 'student/dang_ki_hoc_tap.html', {

    })


def ket_qua_hoc_tap(request):
    student = Student.objects.get(user_ptr=request.user)
    bangDiem = sinhVien_lopTinChiDetail.objects.filter(sinhVien=student).order_by('lopTinChiDetail__semester')

    return render(request, 'student/ket_qua_hoc_tap.html', {
        'bangDiem': bangDiem,
    })

    