from django import forms
from .models import Student, Teacher
from django.core.exceptions import ValidationError
from management.models import lop_chung
from django.contrib.auth.forms import ReadOnlyPasswordHashField

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


class TeacherCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        models = Teacher
        fields = "__all__"

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        teacher = super().save(commit=False)
        teacher.set_password(self.cleaned_data["password1"])
        if commit:
            teacher.save()
        return teacher



