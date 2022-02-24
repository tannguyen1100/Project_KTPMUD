from unicodedata import name
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('info', views.student_info, name='student_info'),
    path('genaral-class', views.genaral_class, name='genaral_class'),
    path('change_info', views.change_info, name="change_info"),
    path('lop_tin_chi_trong_ki', views.lopTC_trong_ki, name='lopTC_trong_ki'),
    path('ket_qua_hoc_tap', views.ket_qua_hoc_tap, name='ket_qua_hoc_tap'),
    path('dang_ki_hoc_tap', views.dang_ki_hoc_tap, name='dang_ki_hoc_tap'),
    path('thoi_khoa_bieu', views.student_timetable, name='student_timetable'),
    path('get/ajax/add_lopTinChi_ajax', views.add_lopTinChi_ajax, name='add_lopTinChi_ajax'),
    path('get/ajax/show_score_ajax', views.show_score_ajax, name='show_score_ajax'),
]
