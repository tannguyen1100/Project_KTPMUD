from django.contrib import admin
from student.forms import lopTinChiForm
from student.forms import timingForm, timingCreationForm
from .models import lop, sinhvien_hocphan, timetable, week, timing
# from vien_dao_tao.admin import StudentInline
# from .forms import TimetableForm
# Register your models here.

class timetableAdmin(admin.ModelAdmin):
    def show_week(self, obj):
        description = ""
        weeks = obj.week.all()
        for week in weeks:
            description = description +"," + (str(week.id))
        return description[1:]
    
    show_week.short_description = "Tuần"

    list_display = ('day', 'show_week')
    list_display_links = ()
    exclude = ()
    # m2m_fields = {"week": admin.HORIZONTAL}

class lopInline(admin.TabularInline):
    model = lop
    extra = 0

class StudentInlinem2m(admin.TabularInline):
    model = lop.sinhVien.through

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

class lopAdmin(admin.ModelAdmin):
    form = lopTinChiForm
    inlines = (StudentInlinem2m,)

admin.site.register(lop, lopAdmin)
admin.site.register(timing, timingAdmin)
admin.site.register(week)
admin.site.register(timetable, timetableAdmin)
admin.site.register(sinhvien_hocphan)



