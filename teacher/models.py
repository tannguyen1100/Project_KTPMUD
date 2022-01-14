from django.db import models

# Create your models here.
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

