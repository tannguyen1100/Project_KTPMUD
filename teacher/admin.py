from django.contrib import admin

from teacher.models import do_an, csvTeacher

class teacherCsvAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'uploaded', 'activated', )
# Register your models here.
admin.site.register(do_an)
admin.site.register(csvTeacher, teacherCsvAdmin)
