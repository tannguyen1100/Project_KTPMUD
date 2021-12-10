from django.forms import ModelForm
from django import forms
from django.forms.widgets import PasswordInput
from users.models import Student
from django.contrib.auth import authenticate

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
    