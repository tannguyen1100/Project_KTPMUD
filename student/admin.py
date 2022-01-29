from django.contrib import admin
from .forms import lopTinChiDetailForm,sinhVien_lopTinChiDetailForm,lopTinChiDetailCreationForm
from .models import csvStudent, lop_tin_chi_detail, sinhVien_lopTinChiDetail, sinhVien_dangKi_lopTinChi
# Register your models here.


class studentCsvAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'uploaded', 'activated', )


class lopTinChiDetailAdmin(admin.ModelAdmin):
    
    add_form = lopTinChiDetailCreationForm
    change_form = lopTinChiDetailForm


    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.form = self.change_form
        else:
            self.form = self.add_form
            
        return super(lopTinChiDetailAdmin, self).get_form(request, obj, **kwargs)

    fieldsets = (
        (None, {'fields': ('lopTinChi','timing', 'timetable', 'teacher','semester',)}),
    )

    list_display = ('__str__', 'semester', 'teacher', )
    ordering = ('semester','lopTinChi')


class sinhVien_lopTinChiDetailAdmin(admin.ModelAdmin):

    change_form = sinhVien_lopTinChiDetailForm

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            pass
        else:
            self.form = self.change_form
            self.inlines = ()
            
        return super(sinhVien_lopTinChiDetailAdmin, self).get_form(request, obj, **kwargs)

class sinhVien_DangKi_lopTinChiAdmin(admin.ModelAdmin):

    list_display = ('sinhVien', 'lopTinChiDetail', 'is_accepted', )
    ordering = ()

admin.site.register(csvStudent ,studentCsvAdmin)
admin.site.register(sinhVien_lopTinChiDetail, sinhVien_lopTinChiDetailAdmin)
admin.site.register(lop_tin_chi_detail, lopTinChiDetailAdmin)
admin.site.register(sinhVien_dangKi_lopTinChi, sinhVien_DangKi_lopTinChiAdmin)



