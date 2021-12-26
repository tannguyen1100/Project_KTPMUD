from django.db import models
from django.db.models.deletion import CASCADE
from management.models import hoc_phan
from django.utils.translation import gettext_lazy as _
from .validators import validate_score
# Create your models here.

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
        verbose_name = "Tuần"
        verbose_name_plural = 'Tuần'

class timetable(models.Model):
    day = models.CharField(choices=DAYS_OF_WEEK, max_length=15)
    week = models.ManyToManyField(week)

    class Meta:
        verbose_name = 'Thời khóa biểu'
        verbose_name_plural = 'Thời khóa biểu'

    def __str__(self):
        return f"{(self.day)} Week {[week.id for week in self.week.all()]}"

class timing(models.Model):
    time_start = models.TimeField(verbose_name="Thời gian bắt đầu")
    time_end = models.TimeField(verbose_name="Thời gian kết thúc")

    class Meta:
        unique_together=('time_start', 'time_end',)
        verbose_name = "Thời gian"
        verbose_name_plural = 'Thời gian'

    def __str__(self):
        return f"{self.time_start.hour}:{self.time_start.minute} - {self.time_end.hour}:{self.time_end.minute}"

class lop(models.Model):
    class ClassType(models.TextChoices):
        LT = "Lý thuyết", "LT"
        TN = "Thí nghiệm", "TN"

    code = models.IntegerField(unique=True)
    type = models.CharField(choices=ClassType.choices, verbose_name="Loại lớp", default=ClassType.LT, max_length=20)
    hoc_phan = models.ForeignKey(hoc_phan, verbose_name="Học phần", related_name="available_class", on_delete=models.CASCADE)
    timetable = models.OneToOneField(timetable, on_delete=CASCADE)
    teacher = models.ForeignKey("users.Teacher", on_delete=models.CASCADE)
    timing = models.ForeignKey(timing, on_delete=CASCADE, null=True)

    def __str__(self):
        return f"{self.code}-{self.hoc_phan}-{self.timetable}-{self.timing}"
    
    class Meta:
        verbose_name = "Lớp tín chỉ"
        verbose_name_plural = 'Lớp tín chỉ'



class sinhvien_hocphan(models.Model):
    sinh_vien=models.ForeignKey('users.Student', on_delete=CASCADE)
    hoc_phan=models.ForeignKey(hoc_phan, on_delete=CASCADE)
    number = models.PositiveSmallIntegerField()
    giua_ki = models.FloatField(verbose_name='Điểm giữa kì', validators=[validate_score], null=True, blank=True)
    cuoi_ki = models.FloatField(verbose_name='Điểm cuối kì' ,validators=[validate_score], null=True, blank=True)

    def __str__(self):
        return f"{self.sinh_vien} {self.hoc_phan}"

    class Meta:
        unique_together = ('sinh_vien', 'hoc_phan', 'number')
        verbose_name = "Bảng điểm"
        verbose_name_plural = "Bảng điểm"




