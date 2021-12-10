from django import forms
from users.models import Teacher
from django.db.models import Q
from .models import vien_dao_tao

class VienCreationForm(forms.ModelForm):
    class Meta:
        models = vien_dao_tao
        fields = ('name', 'code', )

class LopChungAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LopChungAdminForm, self).__init__(*args, **kwargs)
        self.fields['giao_vien'].queryset = Teacher.objects.filter(Q(vien_id=self.instance.vien_id) | Q(vien_id=None))

class VienDaoTaoAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VienDaoTaoAdminForm, self).__init__(*args, **kwargs)
        self.fields['vien_truong'].queryset = Teacher.objects.filter(Q(vien_id=self.instance.id) | Q(vien_id=None))