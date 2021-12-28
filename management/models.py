from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, CharField
from django.db.models.deletion import CASCADE

from django.utils.translation import gettext_lazy as _

# Create your models here.
class vien_dao_tao(models.Model):
    name = CharField(_('Tên viện'), max_length=50, unique=True)
    code = CharField(_("Mã viện"), max_length=10)
    vien_truong = models.ForeignKey("users.Teacher",verbose_name="Viện trưởng", on_delete=models.CASCADE, related_name="vien_quan_ly", blank=True, null=True)

    class Meta:
        verbose_name = "Viện đào tạo"
        verbose_name_plural = 'Viện đào tạo'

    def __str__(self):
        return f"{self.name}"

class khoa(models.Model):
    name = CharField(_('Khóa'), max_length=5, unique=True)

    class Meta:        
        verbose_name = "Khóa"
        verbose_name_plural = 'Khóa'

    def __str__(self):
        return self.name
class lop_chung(models.Model):

    name = CharField(_('Tên lớp'), max_length=15)
    vien = models.ForeignKey(vien_dao_tao, on_delete=models.CASCADE, verbose_name="Viện quản lý",related_name='cac_lop_thuoc_vien')
    giao_vien = models.ForeignKey("users.Teacher",verbose_name="Giáo viên quản lý", on_delete=models.CASCADE, related_name="cac_lop_quan_ly", null=True, blank=True)
    khoa = models.ForeignKey(khoa, on_delete=CASCADE, related_name='lop_cung_khoa', blank=True, null=True, verbose_name="Khóa")
    # capacity = models.IntegerField(default=3)

    class Meta:
        verbose_name = "Lớp chung"
        verbose_name_plural = 'Lớp chung'
        unique_together = ('name', 'khoa')

    def __str__(self):
        return f"{self.name}_{self.khoa}"

class hoc_phan(models.Model):
    name = CharField(_("Tên học phần"), max_length=50)
    code = CharField(_("Mã học phần"), max_length=10, unique=True)
    vien = models.ForeignKey(vien_dao_tao, verbose_name="Viện trực thuộc", on_delete=models.CASCADE, related_name="cac_hoc_phan")
    sinh_vien = models.ManyToManyField('users.Student', verbose_name="Sinh viên", related_name='hocPhan', blank=True)
    class Meta:
        verbose_name = "Học phần"
        verbose_name_plural = 'Học phần'
        ordering = ["vien"]

    def __str__(self):
        return f"{self.name}"
    



