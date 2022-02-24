from msilib.schema import Error
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.urls.base import reverse
from django.forms import formset_factory
from student.models import lop_tin_chi_detail, sinhVien_lopTinChiDetail, sinhVien_dangKi_lopTinChi
from users.models import Student
from management.models import lop_chung, lop_tin_chi, semester
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
        lopTinChiInput = request.POST.get('lopTinChiInput')
        lopDaDangKi = request.POST.getlist('lopDaDangKi[]')
        lopDangKi_format = []
        for lop in lopDaDangKi:
            if lop != "":
                lopDangKi_format.append(lop)

        
        hocPhan_lopTinChiInput = lop_tin_chi.objects.get(code=int(lopTinChiInput)).hocPhan
        hocPhan_lopDangKi = []

        

        for lop in lopDangKi_format:
            hocPhan_lopDangKi.append(lop_tin_chi.objects.get(code=int(lop)).hocPhan)

        print(hocPhan_lopTinChiInput)
        print(hocPhan_lopDangKi)

        if len(lopTinChiInput) != 6:
            response = "Invalid" 
            return JsonResponse({'data': response})
        
        if hocPhan_lopTinChiInput in hocPhan_lopDangKi:
            response = "Invalid hocPhan" 
            return JsonResponse({'data': response})

        else:
            try:
                lopTC_object = lop_tin_chi_detail.objects.get(lopTinChi__code=lopTinChiInput,semester=active_semester )
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

    student = Student.objects.get(user_ptr=request.user)
    active_sem = semester.objects.get(is_active=True)

    current_dangKi_lopTinChi = sinhVien_dangKi_lopTinChi.objects.filter(lopTinChiDetail__semester=active_sem, sinhVien=student)
    current_lopTinChi = []
    for lop in current_dangKi_lopTinChi:
        current_lopTinChi.append(lop.lopTinChiDetail)

    if request.method == "POST":
        lopTinChi = request.POST.getlist('lopTinChiCode')
        deletions = request.POST.getlist('deleteBox')

        lopDangKi = []
        for lop in lopTinChi:
            if lop not in deletions:
                lopDangKi.append(lop)
                
        for lop in lopDangKi:
            lopTinChi_object = lop_tin_chi.objects.get(code=int(lop))
            lopTinChiDetail_object = lop_tin_chi_detail.objects.get(semester=active_sem, lopTinChi=lopTinChi_object)
            try:
                sinhVien_lopTinChiDetail.objects.create(sinhVien=student, lopTinChiDetail=lopTinChiDetail_object)
            except Error as e:
                print(e)

        return render(request, 'student/dang_ki_hoc_tap.html', {
            'message': 'success'
        })
    
    return render(request, 'student/dang_ki_hoc_tap.html', {
        'current_lopTinChi': current_lopTinChi,
    })

def student_timetable(request):
    student = Student.objects.get(user_ptr=request.user)
    active_sem = semester.objects.get(is_active=True)

    thoi_khoa_bieu = sinhVien_dangKi_lopTinChi.objects.filter(lopTinChiDetail__semester=active_sem, sinhVien=student, is_accepted=True)

    current_lopTinChi = []
    for lop in thoi_khoa_bieu:
        current_lopTinChi.append(lop.lopTinChiDetail)

    return render(request, 'student/thoi_khoa_bieu.html', {
        'thoi_khoa_bieu': current_lopTinChi,
    })


def ket_qua_hoc_tap(request):
    student_object = Student.objects.get(user_ptr=request.user)
    first_sem = int(str(student_object.year_start) + "1")
    last_sem = semester.objects.get(is_active=True).name
    semester_objects = semester.objects.filter(name__gte=first_sem, name__lte=last_sem).order_by('-name')
    bangDiem = sinhVien_lopTinChiDetail.objects.filter(sinhVien=student_object).order_by('lopTinChiDetail__semester')

    return render(request, 'student/ket_qua_hoc_tap.html', {
        'all_semester': semester_objects,
        'bangDiem': bangDiem,
    })

def show_score_ajax(request):
    if request.is_ajax():
        student_object = Student.objects.get(user_ptr=request.user)
        sem_instance = request.GET.get('sem')
        sem_object = semester.objects.get(name=sem_instance)
        try:
            bangDiem = sinhVien_lopTinChiDetail.objects.filter(sinhVien=student_object, lopTinChiDetail__semester=sem_object).order_by('lopTinChiDetail__lopTinChi__code')

            data = []
            for bangDiem_instance in bangDiem:

                data.append({
                    'hocPhan': bangDiem_instance.lopTinChiDetail.lopTinChi.hocPhan.name,
                    'giua_ki': bangDiem_instance.giua_ki,
                    'cuoi_ki': bangDiem_instance.cuoi_ki,
                })

            if data == []:
                return JsonResponse({'data': "Not found"})
            else:
                response = data
                return JsonResponse({'data': response})
        except sinhVien_lopTinChiDetail.DoesNotExist:
            return JsonResponse({'data': 'Not found'})
    return JsonResponse({})

    