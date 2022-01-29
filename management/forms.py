from django import forms
from users.models import Teacher
from django.db.models import Q
from .models import vien_dao_tao, timetable, timing
from university_management.forms import TimeInput


class timingCreationForm(forms.ModelForm):
    class Meta:
        model = timing
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time_start'].widget = TimeInput()
        self.fields['time_end'].widget = TimeInput()

class timingForm(forms.ModelForm):
    class Meta:
        model = timing
        fields = "__all__"



class VienCreationForm(forms.ModelForm):
    class Meta:
        models = vien_dao_tao
        fields = ('name', 'code', )

class LopChungForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LopChungForm, self).__init__(*args, **kwargs)
        self.fields['giao_vien'].queryset = Teacher.objects.filter(Q(vien_id=self.instance.vien_id) | Q(vien_id=None))

class VienDaoTaoForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(VienDaoTaoForm, self).__init__(*args, **kwargs)
    #     self.fields['vien_truong'].queryset = Teacher.objects.filter(Q(vien_id=self.instance.id) | Q(vien_id=None))
    pass

