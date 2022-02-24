from email.policy import default
from crispy_forms.layout import Submit
from django import forms
from student.models import csvStudent, lop_tin_chi_detail, sinhVien_lopTinChiDetail
from users.models import Student, Teacher
from crispy_forms.helper import FormHelper

class StudentCsvForm(forms.ModelForm):
    class Meta:
        model = csvStudent
        fields = ('file_name',)


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('firstname', 'surname', 'lastname',"date_of_birth")

    helper = FormHelper()
    helper.add_input(Submit('Submit', 'Submit', css_class='btn-primary'))
    helper.form_method = "POST"


class lopTinChiDetailForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(lopTinChiDetailForm, self).__init__(*args, **kwargs)
        if self.instance.lopTinChi:
            self.fields['teacher'].queryset = Teacher.objects.filter(chuyen_mon=self.instance.lopTinChi.hocPhan.pk)
        
    class Meta:
        model = lop_tin_chi_detail
        fields = '__all__'

class lopTinChiDetailCreationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(lopTinChiDetailCreationForm, self).__init__(*args, **kwargs)
        self.fields['teacher'].queryset = Teacher.objects.none()
        
    class Meta:
        model = lop_tin_chi_detail
        fields = '__all__'
        

class sinhVien_lopTinChiDetailForm(forms.ModelForm):
    class Meta:
        model = sinhVien_lopTinChiDetail
        fields = ('sinhVien', 'lopTinChiDetail', 'giua_ki', 'cuoi_ki', )

class addLopTinChiForm(forms.Form):
    check = forms.BooleanField(initial=False)
    
