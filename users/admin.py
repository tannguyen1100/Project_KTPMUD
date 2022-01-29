# Register your models here.
from django.contrib import admin
from management.admin import LopChungInline
from .models import Student, Teacher
from .forms import StudentCreationForm, TeacherAdminForm, TeacherCreationForm, StudentAdminForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# class StudentInlinem2m(admin.TabularInline):
#     model = Student.lopTC.through
#     extra = 0
#     class Meta:
#         verbose_name = 'Lớp tín chỉ'

class StudentAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    add_form = StudentCreationForm
    change_form = StudentAdminForm

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
            self.inlines = ()
        else:
            self.form = self.change_form
            self.inlines = ()
            
        return super(StudentAdmin, self).get_form(request, obj, **kwargs)

    list_display = ('full_name','code','lop_chung','vien','date_of_birth')
    list_display_links = ('full_name',)
    def full_name(self, obj):
        student = Student.objects.get(user_ptr=obj)
        if student.lastname:
            if student.surname:
                return f"{student.lastname} {student.surname} {student.firstname} {student.code}"
            else:
                return f"{student.lastname} {student.firstname} {student.code}"
        else:
            return f"{student.firstname} {student.code}"

    list_filter = ('vien','lop_chung',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('avatar','firstname', 'lastname', 'surname', 'gender','date_of_birth', 'phone', )}),
        ('Quản lý', {'fields': ('code', ('vien', 'lop_chung'), ('year_start', 'khoa'), )}),
        ('Lớp tín chỉ đăng kí', {'fields': ('lop_tin_chi_dang_ki',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('lastname', 'surname','firstname', 'year_start'),
        }),
    )

    search_fields = ('code','firstname')
    ordering = ('-code',)
    filter_horizontal = ('lop_tin_chi_dang_ki',)


class TeacherAdmin(BaseUserAdmin):

    add_form = TeacherCreationForm
    change_form = TeacherAdminForm

    def fullname(self, obj):
        teacher = Teacher.objects.get(user_ptr=obj)
        return f"{teacher.lastname} {teacher.surname} {teacher.firstname}"

    fullname.short_description = "Tên"

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
            self.inlines = ()
        else:
            self.form = self.change_form
            self.inlines = ()
            
        return super(TeacherAdmin, self).get_form(request, obj, **kwargs)

    list_display = ('fullname', 'vien', 'date_of_birth')
    list_filter = ('vien',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'year_start',)}),
        ('Personal info', {'fields': ('firstname', 'lastname','surname', 'gender','date_of_birth',)}),
        ('Quản lý', {'fields': ('vien',)}),
        ('Chuyên môn', {'fields': ('chuyen_mon',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('lastname', 'surname', 'firstname', ),
        }),
    )

    search_fields = ('email','firstname')
    ordering = ('vien',)
    filter_horizontal = ('chuyen_mon',)


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)



