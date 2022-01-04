from re import template
from django.urls import path

from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('login/post/ajax/login_validate', views.login_validate, name='login_validate'),
    path('logout', views.logout_view, name='logout'),
    path('forget_password', views.forget_password, name="forget_password"),
    path('password_reset_comfirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='user\password_reset_comfirm.html'), name="password_reset_confirm"),
    path('password_reset_done', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_done.html'), name='password_reset_complete'),      
]