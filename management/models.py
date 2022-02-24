from django.db import models
from django.db.models.fields import CharField
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
from management.validators import validate_semester

# Create your models here.
class vien_dao_tao(models.Model):
    name = CharField(_('Tên viện'), max_length=50, unique=True)
    code = CharField(_("Mã viện"), max_length=10)
    vien_truong = models.ForeignKey("users.Teacher",verbose_name="Viện trưởng", on_delete=models.CASCADE, related_name="vien_quan_ly", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Viện đào tạo"
        verbose_name_plural = '1. Viện đào tạo'

class csv_vienDaoTao(models.Model):
    file_name = models.FileField(_("Học phần CSV file"), upload_to='hocphan_csv', max_length=100)
    uploaded = models.DateTimeField(_("Uploaded time"), auto_now_add=True)
    activated = models.BooleanField(default=True)

    def __str__(self):
        return f"File id: {self.id} "

    class Meta:
        verbose_name = "Thêm viện đào tạo từ file CSV"
        verbose_name_plural = "Thêm viện đào tạo từ file CSV"



class khoa(models.Model):
    name = CharField(_('Khóa'), max_length=5, unique=True)

    def __str__(self):
        return self.name
    class Meta:        
        verbose_name = "3. Khóa"
        verbose_name_plural = '3. Khóa'

    
class lop_chung(models.Model):

    name = CharField(_('Tên lớp'), max_length=15)
    vien = models.ForeignKey("management.vien_dao_tao", on_delete=models.CASCADE, verbose_name="Viện quản lý",related_name='cac_lop_thuoc_vien')
    giao_vien = models.ForeignKey("users.Teacher",verbose_name="Giáo viên quản lý", on_delete=models.CASCADE, related_name="cac_lop_quan_ly", null=True, blank=True)
    khoa = models.ForeignKey("management.khoa", on_delete=CASCADE, related_name='lop_cung_khoa', blank=True, null=True, verbose_name="Khóa")

    def __str__(self):
        return f"{self.name}_{self.khoa}"
    class Meta:
        verbose_name = "5. Lớp chung"
        verbose_name_plural = '5. Lớp chung'
        unique_together = ('name', 'khoa')

class lop_tin_chi(models.Model):
    class ClassType(models.TextChoices):
        LT = "LT", "LT"
        TN = "TN", "TN"
        LT_BT = "LT+BT", "LT+BT"

    code = models.IntegerField(unique=True, verbose_name="Mã lớp")
    type = models.CharField(choices=ClassType.choices, verbose_name="Loại lớp", default=ClassType.LT, max_length=20)
    hocPhan = models.ForeignKey("management.hoc_phan", verbose_name="Học phần", related_name="available_class", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.code}-{self.hocPhan}"
    
    class Meta:
        verbose_name = "9. Lớp tín chỉ"
        verbose_name_plural = '9. Lớp tín chỉ'

class csv_lopTinChi(models.Model):
    file_name = models.FileField(_("Học phần CSV file"), upload_to='hocphan_csv', max_length=100)
    uploaded = models.DateTimeField(_("Uploaded time"), auto_now_add=True)
    activated = models.BooleanField(default=True)

    def __str__(self):
        return f"File id: {self.id}"

    class Meta:
        verbose_name = "Thêm lớp tín chỉ từ file CSV"
        verbose_name_plural = "Thêm lớp tín chỉ từ file CSV"

class hoc_phan(models.Model):
    name = CharField(_("Tên học phần"), max_length=50)
    code = CharField(_("Mã học phần"), max_length=10, unique=True)
    vien = models.ForeignKey("management.vien_dao_tao", verbose_name="Viện trực thuộc", on_delete=models.CASCADE, related_name="cac_hoc_phan")
    required_hocPhan = models.ForeignKey("management.hoc_phan", verbose_name="Học phần kiên quyết", on_delete=models.CASCADE, null=True, blank=True, default=None)
    class Meta:
        verbose_name = "2. Học phần"
        verbose_name_plural = '2. Học phần'
        ordering = ["vien"]

    def __str__(self):
        return f"{self.name}"

class csv_hocPhan(models.Model):
    file_name = models.FileField(_("Học phần CSV file"), upload_to='hocphan_csv', max_length=100)
    uploaded = models.DateTimeField(_("Uploaded time"), auto_now_add=True)
    activated = models.BooleanField(default=True)

    def __str__(self):
        return f"File id: {self.id}"

    class Meta:
        verbose_name = "Thêm học phần từ file CSV"
        verbose_name_plural = "Thêm học phần từ file CSV"


class semester(models.Model):
    name = models.IntegerField(_("Kì"), unique=True, validators=[validate_semester])
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "4. Kì"
        verbose_name_plural = '4. Kì'
        ordering = ["name"]
    
class csv_semester(models.Model):
    file_name = models.FileField(_("Semester CSV file"), upload_to='semester_csv', max_length=100)
    uploaded = models.DateTimeField(_("Uploaded time"), auto_now_add=True)
    activated = models.BooleanField(default=True)

    def __str__(self):
        return f"File id: {self.id} "

    class Meta:
        verbose_name = "Thêm kì học từ file CSV"
        verbose_name_plural = "Thêm kì học từ file CSV"

    
DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)

class week(models.Model):
    id = models.IntegerField(verbose_name='Tuần', primary_key=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "7. Tuần"
        verbose_name_plural = '7. Tuần'

class csvWeek(models.Model):
    file_name = models.FileField(_("Week CSV file"), upload_to='quanLy_csvs', max_length=100)
    uploaded = models.DateTimeField(_("Uploaded time"), auto_now_add=True)
    activated = models.BooleanField(default=True)

    def __str__(self):
        return f"File id: {self.id}"

    class Meta:
        verbose_name = "Thêm tuần học từ file CSV"
        verbose_name_plural = "Thêm tuần học từ file CSV"

class timetable(models.Model):
    day = models.CharField(choices=DAYS_OF_WEEK, max_length=15)
    week = models.ManyToManyField(week)

    def display_week(self):
        all_week = self.week.all()
        len_week = all_week.count()
        display_week = ''
        display_week = display_week + str(all_week[0].id) + "-"

        for i in range(len_week-1):
            if all_week[i+1].id == all_week[i].id + 1:
                continue
            else:
                display_week = display_week + str(all_week[i].id) + "," + str(all_week[i+1].id)

        display_week = display_week + "-" + str(all_week[len_week-1].id)

        return display_week
                
    def __str__(self):
        return f"{(self.day)} {self.display_week()}"

    
    class Meta:
        verbose_name = '8. Thời khóa biểu'
        verbose_name_plural = '8. Thời khóa biểu'



class csvTimetable(models.Model):
    file_name = models.FileField(_("Timetable CSV file"), upload_to='quanLy_csvs', max_length=100)
    uploaded = models.DateTimeField(_("Uploaded time"), auto_now_add=True)
    activated = models.BooleanField(default=True)

    def __str__(self):
        return f"File id: {self.id}"

    class Meta:
        verbose_name = "Thêm thời khóa biểu từ file CSV"
        verbose_name_plural = "Thêm thời khóa biểu từ file CSV"

class timing(models.Model):
    time_start = models.TimeField(verbose_name="Thời gian bắt đầu")
    time_end = models.TimeField(verbose_name="Thời gian kết thúc")


    def __str__(self):
        return f"{self.time_start.hour}:{self.time_start.minute} - {self.time_end.hour}:{self.time_end.minute}"

    class Meta:
        unique_together=('time_start', 'time_end',)
        verbose_name = "6. Thời gian"
        verbose_name_plural = '6. Thời gian'

class csvTiming(models.Model):
    file_name = models.FileField(_("TimingCSV file"), upload_to='quanLy_csvs', max_length=100)
    uploaded = models.DateTimeField(_("Uploaded time"), auto_now_add=True)
    activated = models.BooleanField(default=True)

    def __str__(self):
        return f"File id: {self.id}"   

    class Meta:
        verbose_name = "Thêm thời gian từ file CSV"
        verbose_name_plural = "Thêm thời gian từ file CSV" 





