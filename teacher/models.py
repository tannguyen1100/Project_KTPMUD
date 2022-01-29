from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class csvTeacher(models.Model):
    file_name = models.FileField(_("Teacher CSV file"), upload_to='teacher_csvs', max_length=100)
    uploaded = models.DateTimeField(_("Uploaded time"), auto_now_add=True)
    activated = models.BooleanField(default=True)

    def __str__(self):
        return f"File id: {self.id}"

    class Meta:
        verbose_name = "Thêm giáo viên từ file CSV"
        verbose_name_plural = "Thêm giáo viên từ file CSV"

class do_an(models.Model):
    name = models.CharField(max_length=50, verbose_name='Tên đồ án')
    slug_name = models.SlugField(unique=True, null=True)
    teacher = models.ManyToManyField('users.Teacher', verbose_name='Giáo viên', related_name='do_an_tham_gia')
    student = models.ManyToManyField('users.Student', verbose_name='Sinh viên', related_name='do_an_tham_gia')
    start_time = models.DateField(null=True, blank=True)
    end_time = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = "Đồ án"
        verbose_name_plural = "Đồ án"

