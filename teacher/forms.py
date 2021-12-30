from django import forms

class ChangeDiemForm(forms.Form):
    sinh_vien = forms.CharField(max_length=15, label="Họ và tên", widget=forms.TextInput(attrs={'readonly': True, 'border': False}))
    code = forms.CharField(max_length=15, label="Mã số sinh viên", widget=forms.TextInput(attrs={'readonly': True, 'border': False}))
    giua_ki = forms.FloatField(max_value=10, min_value=0, required=False, label="Điểm giữa kì")
    cuoi_ki = forms.FloatField(max_value=10, min_value=0, required=False, label='Điểm cuối kì')


