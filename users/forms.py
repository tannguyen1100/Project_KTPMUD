from django import forms
from .models import Student, Teacher
from management.models import lop_chung
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# forms.DateInput.input_type='date'

class StudentCreationForm(forms.ModelForm):

    class Meta:
        models = Student
        fields = "__all__"


class StudentAdminForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    def __init__(self, *args, **kwargs):
        super(StudentAdminForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.fields['lop_chung'].queryset = lop_chung.objects.filter(vien_id=self.instance.vien_id)

    class Meta:
        model = Student
        fields = "__all__"
    
class TeacherCreationForm(forms.ModelForm):

    class Meta:
        models = Teacher
        fields = "__all__"

class TeacherAdminForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()


    

