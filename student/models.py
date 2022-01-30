from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
from .validators import validate_score
# Create your models here.

class csvStudent(models.Model):
    file_name = models.FileField(_("Student CSV file"), upload_to='student_csvs', max_length=100)
    uploaded = models.DateTimeField(_("Uploaded time"), auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"

    class Meta:
        verbose_name = "Thêm sinh viên từ file CSV"
        verbose_name_plural = "Thêm sinh viên từ file CSV"



class lop_tin_chi_detail(models.Model):
    lopTinChi = models.ForeignKey("management.lop_tin_chi",verbose_name="Lớp tín chỉ", on_delete=CASCADE, related_name="detail")
    semester = models.ForeignKey("management.semester", verbose_name="Kì", related_name="available_class", on_delete=models.CASCADE)
    timetable = models.ForeignKey("management.timetable", on_delete=models.CASCADE)
    timing = models.ForeignKey("management.timing", on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey("users.Teacher", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.lopTinChi.code}-Kì {self.semester}"
    
    class Meta:
        verbose_name = "Lớp tín chỉ chi tiết"
        verbose_name_plural = 'Lớp tín chỉ chi tiết'
        unique_together = ('lopTinChi', 'semester')


class sinhVien_lopTinChiDetail(models.Model):
    sinhVien = models.ForeignKey('users.Student', verbose_name="Sinh viên", on_delete=models.CASCADE, related_name='lopTinChiThamGia')
    lopTinChiDetail = models.ForeignKey("student.lop_tin_chi_detail", verbose_name='Lớp tín chỉ', on_delete=models.CASCADE)
    giua_ki = models.FloatField(verbose_name='Điểm giữa kì', validators=[validate_score], null=True, blank=True)
    cuoi_ki = models.FloatField(verbose_name='Điểm cuối kì' ,validators=[validate_score], null=True, blank=True)

    def __str__(self):
        return f"{self.sinhVien} {self.lopTinChiDetail.lopTinChi.hocPhan} "

    class Meta:
        unique_together = ('sinhVien', 'lopTinChiDetail')
        verbose_name = "Bảng điểm"
        verbose_name_plural = "Bảng điểm"

class sinhVien_dangKi_lopTinChi(models.Model):
    sinhVien = models.ForeignKey('users.Student', verbose_name="Sinh viên", on_delete=models.CASCADE, related_name='lopTinChiĐangKi')
    lopTinChiDetail = models.ForeignKey("student.lop_tin_chi_detail", verbose_name='Lớp tín chỉ', on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.sinhVien} đăng kí lớp {self.lopTinChiDetail.lopTinChi.code} "

    class Meta:
        unique_together = ('sinhVien', 'lopTinChiDetail')
        verbose_name = "Sinh viên đăng kí lớp tín chỉ"
        verbose_name_plural = "Sinh viên đăng kí lớp tín chỉ"
    




