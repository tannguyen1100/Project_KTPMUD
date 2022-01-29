from django.contrib import admin
from users.models import Student, Teacher
from .models import  csv_lopTinChi, semester, vien_dao_tao, lop_chung, hoc_phan, khoa, timetable, week, timing, lop_tin_chi
from .forms import LopChungForm, VienDaoTaoForm, VienCreationForm, timingCreationForm, timingForm
from .models import csvTimetable, csvTiming, csvWeek, csv_hocPhan, csv_semester, csv_vienDaoTao

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
    form = LopChungForm
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
    change_form = VienDaoTaoForm

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
            self.inlines = [
                LopChungInline,
                ]
        else:
            self.form = self.change_form
            self.inlines = [
                LopChungInline,
                TeacherInline,
                ]

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
        TeacherInline,
        LopChungInline,
    ]


class timingAdmin(admin.ModelAdmin):

    add_form = timingCreationForm
    change_form = timingForm

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
            self.inlines = ()
        else:
            self.form = self.change_form
            self.inlines = ()
            
        return super(timingAdmin, self).get_form(request, obj, **kwargs)

    ordering = ("time_start",)

class timetableAdmin(admin.ModelAdmin):
    # def show_week(self, obj):
    #     description = ""
    #     weeks = obj.week.all()
    #     for week in weeks:
    #         description = description +"," + (str(week.id))
    #     return description[1:]
    
    # show_week.short_description = "Tuần"

    list_display = ('day','__str__')
    list_display_links = ()
    exclude = ()



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

    form = LopChungForm

    list_display = ('__str__', 'vien','giao_vien')
    list_filter = ('vien','khoa')
    
    search_fields = ('name',)
    ordering = ('khoa',)

    inlines = [
        StudentInline,
    ]

class lopTinChiAdmin(admin.ModelAdmin):
    fields = ("code", "type", "hocPhan", )

class HocPhanAdmin(admin.ModelAdmin):

    fields = ('name','code','vien','required_hocPhan')
    list_display = ('name','vien',)
    list_filter = ('vien',)
    
    search_fields = ('name',)
    ordering = ('vien',)
    filter_horizontal = ()



class hocPhanCsvAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'uploaded', 'activated', )

class semesterCsvAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'uploaded', 'activated', )

class semesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active',)


class timingCsvAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'uploaded', 'activated', )

class weekCsvAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'uploaded', 'activated', )

class timetableCsvAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'uploaded', 'activated', )

class vienDaoTaoCsvAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'uploaded', 'activated', )

class lopTinChiCsvAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'uploaded', 'activated', )



admin.site.register(vien_dao_tao,VienAdmin)
admin.site.register(lop_chung, LopChungAdmin)
admin.site.register(hoc_phan, HocPhanAdmin)
admin.site.register(lop_tin_chi, lopTinChiAdmin)
admin.site.register(khoa)
admin.site.register(semester, semesterAdmin)
admin.site.register(timing, timingAdmin)
admin.site.register(week)
admin.site.register(timetable, timetableAdmin)

admin.site.register(csv_semester, semesterCsvAdmin)
admin.site.register(csvTiming ,timingCsvAdmin)
admin.site.register(csvWeek ,weekCsvAdmin)
admin.site.register(csvTimetable ,timetableCsvAdmin)
admin.site.register(csv_vienDaoTao ,vienDaoTaoCsvAdmin)
admin.site.register(csv_hocPhan, hocPhanCsvAdmin)
admin.site.register(csv_lopTinChi, lopTinChiCsvAdmin)





