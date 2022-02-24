import code
from django.db.models.signals import post_save
from django.dispatch import receiver
import csv
from .models import csv_hocPhan, csv_lopTinChi, csv_semester, csvTimetable, csvTiming, csvWeek, csv_vienDaoTao, lop_tin_chi
from .models import timetable, week, hoc_phan, semester, vien_dao_tao, timing, timetable
from django.db import IntegrityError



@receiver(post_save, sender=csv_hocPhan)
def create_hocPhan_from_csv(sender, instance, created, **kwargs):
    csv_file = instance.file_name
    activated = instance.activated
    if activated:
        with open(csv_file.path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                try:
                    hocPhan = hoc_phan.objects.create(
                        name=row[0],
                        code=row[1],
                        vien=vien_dao_tao.objects.get(pk=row[2]),
                    )                 
                    hocPhan.save()
                except IndexError:
                    print(i)

@receiver(post_save, sender=csv_semester)
def create_semester_from_csv(sender, instance, created, **kwargs):
    csv_file = instance.file_name
    activated = instance.activated
    if activated:
        with open(csv_file.path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                try:
                    sem = semester.objects.create(
                        name=int(row[0]),
                    )                 
                    sem.save()
                except IndexError:
                    print(i)

@receiver(post_save, sender=semester)
def activate_semester(sender, instance, created, **kwargs):
    if instance.is_active == True:
        other_semesters = semester.objects.exclude(pk=instance.pk)
        for sem in other_semesters:
            sem.is_active = False
            sem.save()

@receiver(post_save, sender=csvTimetable)
def create_timetable_from_csv(sender, instance, created, **kwargs):
    csv_file = instance.file_name
    activated = instance.activated
    if activated:
        with open(csv_file.path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                try:
                    timeTable = timetable.objects.create(
                        day=row[0],
                    )  
                    week_list = row[1].split(" ")      
                    for w in week_list:
                        week_object = week.objects.get(id=int(w))
                        timeTable.week.add(week_object)      

                    timeTable.save()
                except IndexError:
                    print(i)


@receiver(post_save, sender=csvTiming)
def create_timing_from_csv(sender, instance, created, **kwargs):
    csv_file = instance.file_name
    activated = instance.activated
    if activated:
        with open(csv_file.path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                try:
                    timing_object = timing.objects.create(
                        time_start=row[0],
                        time_end=row[1],
                    )
                    timing_object.save()
                except (IndexError, IntegrityError) as e:
                    print(e)
                    pass

@receiver(post_save, sender=csvWeek)
def create_week_from_csv(sender, instance, created, **kwargs):
    csv_file = instance.file_name
    activated = instance.activated
    if activated:
        with open(csv_file.path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                try:
                    week_object = week.objects.create(
                        id=row[0]
                    )
                    week_object.save()
                except (IndexError, IntegrityError) as e:
                    print(e)
                    pass

@receiver(post_save, sender=csv_vienDaoTao)
def create_week_from_csv(sender, instance, created, **kwargs):
    csv_file = instance.file_name
    activated = instance.activated
    if activated:
        with open(csv_file.path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                try:
                    vienDaoTao_object = vien_dao_tao.objects.create(
                        name=row[0],
                        code=row[1]
                    )
                    vienDaoTao_object.save()
                except (IndexError, IntegrityError) as e:
                    print(e)

@receiver(post_save, sender=csv_lopTinChi)
def create_lopTinChi_from_csv(sender, instance, created, **kwargs):
    csv_file = instance.file_name
    activated = instance.activated
    if activated:
        with open(csv_file.path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                try:
                    hocPhan_instance = hoc_phan.objects.get(code=row[2])
                    lopTinChi_object = lop_tin_chi.objects.create(
                        code=row[0],
                        type=row[1],
                        hocPhan=hocPhan_instance
                    )
                   
                    lopTinChi_object.save()
                except (IndexError, IntegrityError) as e:
                    print(e)


