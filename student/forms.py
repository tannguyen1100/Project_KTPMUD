from django.db.models.query import EmptyQuerySet
from django.forms import ModelForm
from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth import authenticate
from users.models import Student, Teacher
from student.models import timing, lop
from university_management.forms import TimeInput

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = ('firstname', 'lastname',"date_of_birth")
        
class StudentLoginForm(ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("This user not exist")

        return super(StudentLoginForm, self).clean(*args, **kwargs)
    

class timingCreationForm(ModelForm):
    class Meta:
        model = timing
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time_start'].widget = TimeInput()
        self.fields['time_end'].widget = TimeInput()

class timingForm(ModelForm):
    class Meta:
        model = timing
        fields = "__all__"


class lopTCAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(lopTCAdminForm, self).__init__(*args, **kwargs)
        self.fields['teacher'].queryset = Teacher.objects.filter(chuyen_mon=self.instance.hoc_phan_id)
        try:
            print(1)
            hocPhan = self.instance.hoc_phan
        except:
            print(2)

        print(self.fields['hoc_phan'].queryset)
        # if not isinstance(hocPhan, EmptyQuerySet) :
        #     self.fields['sinh_vien'].queryset = hocPhan.sinh_vien.all()
        
        


    class Meta:
        model = lop
        fields = '__all__'
        

class sinhVien_hocPhanForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(sinhVien_hocPhanForm, self).__init__(*args, **kwargs)
    #     self.fields['sinh_vien'].queryset = Student.objects.all()
    pass
    
