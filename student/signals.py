from django.db.models.signals import post_save
from django.dispatch import receiver
import csv
from student.admin import lopTinChiDetailAdmin
from users.models import Student
from management.models import vien_dao_tao, lop_chung
from .models import csvStudent, sinhVien_dangKi_lopTinChi, sinhVien_lopTinChiDetail

@receiver(post_save, sender=csvStudent)
def create_student_from_csv(sender, instance, created, **kwargs):
    csv_file = instance.file_name
    activated = instance.activated
    if activated:
        with open(csv_file.path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                try:
                    student = Student.objects.create(
                        lastname = row[0], 
                        surname = row[1],
                        firstname = row[2],
                        gender = row[3],
                        year_start = row[4],
                        date_of_birth = row[5],
                    )
                    student.save()
                    student.vien = vien_dao_tao.objects.get(pk=int(row[6]))
                    student.lop_chung = lop_chung.objects.get(pk=int(row[7]))
                    student.save()
                except IndexError:
                    print(i)


@receiver(post_save, sender=sinhVien_dangKi_lopTinChi)
def create_bangDiem_from_DangKi(sender, instance, created, **kwargs):
    if instance.is_accepted:
        sinhVien_lopTinChiDetail.objects.create(
            sinhVien = instance.sinhVien,
            lopTinChiDetail = instance.lopTinChiDetail,
        )
        
