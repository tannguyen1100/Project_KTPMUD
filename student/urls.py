from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('info', views.student_info, name='student_info'),
    path('genaral-class', views.genaral_class, name='genaral_class'),
    path('change_info', views.change_info, name="change_info"),
]
