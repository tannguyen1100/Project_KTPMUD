from django.db.models.signals import post_save
from django.dispatch import receiver
import csv
from users.models import Teacher
from management.models import vien_dao_tao
from .models import csvTeacher

@receiver(post_save, sender=csvTeacher)
def create_teacher_from_csv(sender, instance, created, **kwargs):
    csv_file = instance.file_name
    activated = instance.activated
    if activated:
        with open(csv_file.path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                try:
                    teacher = Teacher.objects.create(
                        lastname = row[0], 
                        surname = row[1],
                        firstname = row[2],
                        gender = row[3],
                        year_start = row[4],
                        date_of_birth = row[5],
                    )
                    teacher.save()
                    teacher.vien = vien_dao_tao.objects.get(pk=int(row[6]))
                    teacher.save()
                except IndexError:
                    print(i)
