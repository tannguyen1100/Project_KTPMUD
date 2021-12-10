# Register your models here.
from django.contrib import admin
from .models import Student, Teacher
from .forms import StudentCreationForm, TeacherCreationForm, StudentAdminForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.urls import reverse
from django.utils.html import format_html

class StudentAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    add_form = StudentCreationForm
    form = StudentAdminForm

    list_display = ('full_name','code','lop_chung', "view_vien_link",)

    def full_name(self, obj):
        student = Student.objects.get(user_ptr=obj)
        return f"{student.lastname} {student.surname} {student.firstname}"

    def view_vien_link(self, obj):
        student = Student.objects.get(user_ptr=obj)
        vien = student.vien
        url = (
            reverse("admin:vien_dao_tao_vien_dao_tao_changelist") + f"{vien.id}"
        )
        return format_html("<a href={} > {} </a>", url, vien)
    view_vien_link.short_description = "Viện quản lý"


    list_filter = ('vien','lop_chung',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('firstname', 'lastname', 'surname', 'gender','date_of_birth', 'code', )}),
        ('Quản lý', {'fields': ('vien', 'lop_chung', 'year_start', 'khoa', )}),
        ('Permissions', {'fields': ()}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('firstname', 'lastname', 'surname'),
        }),
    )

    search_fields = ('code','firstname')
    ordering = ('code',)


class TeacherAdmin(BaseUserAdmin):

    add_form = TeacherCreationForm

    list_display = ('email','firstname', 'vien')
    list_filter = ('vien',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'year_start',)}),
        ('Personal info', {'fields': ('firstname', 'lastname', 'gender','date_of_birth',)}),
        ('Quản lý', {'fields': ('vien',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),
        }),
    )

    search_fields = ('email','firstname')
    ordering = ('vien',)
    filter_horizontal = ()

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)



