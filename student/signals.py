from django.db.models.signals import post_save
from django.dispatch import receiver
import csv
from users.models import Student

from student.models import csvStudent

@receiver(post_save, sender=csvStudent)
def create_student_from_csv(sender, instance, created, **kwargs):
    csv_file = instance.file_name
    activated = instance.activated
    if activated:
        with open(csv_file.path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                student = Student.objects.create(
                    lastname = row[0], 
                    surname = row[1],
                    firstname = row[2],
                    gender = row[3],
                    year_start = row[4],
                    date_of_birth = row[5]
                )
                student.save()
