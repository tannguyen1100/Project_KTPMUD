from django import forms
from users.models import Teacher, Student
from teacher.models import do_an
import re


class ChangeDiemForm(forms.Form):
    sinh_vien = forms.CharField(max_length=15, label="Họ và tên", widget=forms.TextInput(attrs={'readonly': True, 'border': False}))
    code = forms.CharField(max_length=15, label="Mã số sinh viên", widget=forms.TextInput(attrs={'readonly': True, 'border': False}))
    giua_ki = forms.FloatField(max_value=10, min_value=0, required=False, label="Điểm giữa kì")
    cuoi_ki = forms.FloatField(max_value=10, min_value=0, required=False, label='Điểm cuối kì', )


class DoAnForm(forms.Form):

    name = forms.CharField(max_length=150, label="Tên đồ án", widget=forms.TextInput(attrs={'border': False}), required=True)
    slug_name = forms.SlugField()
    giao_vien = forms.CharField(max_length=1000, label='Giáo viên tham gia')
    sinh_vien = forms.CharField(max_length=1000, label='Sinh viên tham gia')

    start_time = forms.DateField(required=True, widget=forms.DateInput(format='%d/%m/%Y'), input_formats=('%d/%m/%Y', ))
    end_time = forms.DateField(required=False, widget=forms.DateInput(format='%d/%m/%Y'), input_formats=('%d/%m/%Y', ))
    class Meta:
        fields = "__all__"


    def save(self):
        data = self.cleaned_data
        name = data['name']
        slug_name_field = data['slug_name']
        start_time = data['start_time']
        end_time = data['end_time']
        sinh_vien = re.findall(r"\d+", data['sinh_vien'])
        giao_vien = data['giao_vien'].replace(" ", "").split(",")

        updated_values = {'start_time': start_time, 'end_time': end_time}
        
        doAn, created = do_an.objects.update_or_create(slug_name=slug_name_field, name=name, defaults=updated_values)

        doAn.student.clear()
        doAn.teacher.clear()

        for sinhVien in sinh_vien:
            studentInstance = Student.objects.get(code=sinhVien)
            doAn.student.add(studentInstance)

        for giaoVien in giao_vien:
            teacherInstance = Teacher.objects.get(email=giaoVien)
            doAn.teacher.add(teacherInstance)
