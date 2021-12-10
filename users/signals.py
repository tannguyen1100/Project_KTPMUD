from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from . import unidecode
from .emails import save_raw_password, send_raw_password

from .models import Student, Teacher

@receiver(post_save, sender=Student)
def student_send_raw_password(sender, instance, created, **kwargs):
    if instance.password == "":
        auto_password = Student.objects.make_random_password()
        send_raw_password(instance, auto_password)
        save_raw_password(auto_password)
        instance.set_password(auto_password)
        instance.save()



@receiver(pre_save, sender=Student)
def pre_save_set_student_email(sender, instance, **kwargs):
    email = unidecode.name_2_email(ten=instance.firstname, ho=instance.lastname, dem=instance.surname, code=instance.code)
    instance.email = email

@receiver(pre_save, sender=Student)
def pre_save_create_khoa(sender, instance, **kwargs):
    student_khoa = str(instance.year_start - 1955)
    student_khoa = "K" + student_khoa
    if instance.khoa != student_khoa:
        instance.khoa = student_khoa

@receiver(pre_save, sender=Student)
def pre_save_set_student_role(sender, instance, **kwargs):
    if instance.role != 0:
        instance.role = 0
    
@receiver(pre_save, sender=Teacher)
def pre_save_set_teacher_role(sender, instance, **kwargs):
    if instance.role != 1:
        instance.role = 1



