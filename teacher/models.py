from django.db import models
import datetime

# Create your models here.
class do_an(models.Model):
    name = models.CharField(max_length=50, verbose_name='Tên đồ án')
    teacher = models.ManyToManyField('users.Teacher', verbose_name='Giáo viên', related_name='do_an_tham_gia')
    student = models.ManyToManyField('users.Student', verbose_name='Sinh viên', related_name='do_an_tham_gia')
    start_time = models.DateField(default=datetime.datetime.now().year)
    end_time = models.DateField(default=datetime.datetime.now().year)
    

