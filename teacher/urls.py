from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [
    path('info', views.info, name='info'),

    path('lop_chung_quan_ly', views.lop_chung_quan_ly, name='lop_chung_quan_ly'),
    path('<int:student_code>', views.info_student, name='info_student'),
    path('lop_chung_quan_ly/<str:ten_lop_chung>', views.tung_lop_chung, name='tung_lop_chung'),
    path('', views.search_student, name="search_student"),

    path('lop_tin_chi', views.lop_tin_chi_ql, name='lop_tin_chi_ql'),
    path('lop_tin_chi/<str:sem>/<int:lopTC_code>', views.tung_lop_TC, name='tung_lop_TC'),
    path('do_an', views.do_an_view, name='do_an'),
    path('do_an/add', views.them_do_an, name='them_do_an'),
    path('do_an/<str:slug_name>/change', views.tung_do_an, name='tung_do_an'),
    path('search', views.search, name='search'),
    path('get/ajax/search_student', views.search_student_ajax, name='search_student_ajax'),

]
