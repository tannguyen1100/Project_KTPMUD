from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [
    path('info', views.info, name='info'),

    path('lop_chung_quan_ly', views.lop_chung_quan_ly, name='lop_chung_quan_ly'),
    path('lop_chung_quan_ly/<str:ten_lop_chung>', views.tung_lop_chung, name='tung_lop_chung'),
    path('<int:student_code>', views.info_student, name='info_student'),

    path('lop_tin_chi', views.lop_tin_chi_ql, name='lop_tin_chi_ql'),

]
