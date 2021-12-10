from django.contrib import admin
from users.models import Student, Teacher
from management.models import vien_dao_tao, lop_chung, hoc_phan
from django import forms
from .forms import LopChungAdminForm, VienDaoTaoAdminForm, VienCreationForm
# Register your models here.

class StudentInline(admin.TabularInline):
    model = Student
    fields = ('email',)
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return False

class LopChungInline(admin.TabularInline):
    model = lop_chung
    form = LopChungAdminForm
    extra = 0

 


class TeacherInline(admin.TabularInline):
    model = Teacher
    fields = ('email',)
    extra = 0
    
    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class HocPhanInline(admin.TabularInline):
    model = hoc_phan
    fields = ('name','code')
    extra = 0


class VienAdmin(admin.ModelAdmin):

    add_form = VienCreationForm
    change_form = VienDaoTaoAdminForm

    
    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
        else:
            self.form = self.change_form

        return super(VienAdmin, self).get_form(request, obj, **kwargs)

    list_display = ('name','code','vien_truong')
    list_filter = ()

    search_fields = ('name',)
    ordering = ('name',)

        
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'code',),
        }),
    )

    inlines = [
        LopChungInline,
        TeacherInline,
        HocPhanInline,
        StudentInline
    ]

class StudentInline(admin.TabularInline):
    model = Student
    fields = ('email','firstname')
    ordering = ('email',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class LopChungAdmin(admin.ModelAdmin):

    form = LopChungAdminForm

    list_display = ('name','vien','giao_vien')
    list_filter = ('vien',)
    
    search_fields = ('name',)
    ordering = ('vien',)

    inlines = [
        StudentInline,
    ]

class HocPhanAdmin(admin.ModelAdmin):

    fields = ('name','code','vien',)
    list_display = ('name','vien',)
    list_filter = ('vien',)
    
    search_fields = ('name',)
    ordering = ('vien',)

admin.site.register(vien_dao_tao,VienAdmin)
admin.site.register(lop_chung, LopChungAdmin)
admin.site.register(hoc_phan, HocPhanAdmin)

