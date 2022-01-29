from itertools import count
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from . import unidecode
from .emails import save_raw_password, send_raw_password
from .models import Student, Teacher
from management.models import khoa


@receiver(pre_save, sender=Student)
def pre_save_set_student_role(sender, instance, **kwargs):
    if instance.role != 0:
        instance.role = 0

@receiver(post_save, sender=Student)
def post_save_set_student_khoa(sender, instance, created, **kwargs):
    instance_yearStart = instance.year_start
    khoa_number = int(instance_yearStart) - 1955
    khoa_instance, created = khoa.objects.get_or_create(
        name= f'K{khoa_number}',
    )
    instance.khoa = khoa_instance    

@receiver(post_save, sender=Student)
def post_save_set_student_code(sender, instance, created, **kwargs):
    instance_yearStart = instance.year_start
    studentList = Student.objects.raw('SELECT *, ROW_NUMBER() OVER( ORDER BY user_ptr_id) as "stt" from users_student where year_start= %s', [instance_yearStart])
    stt_instanceStudent = str(studentList[-1].stt)
    while len(stt_instanceStudent) < 4:
        stt_instanceStudent = "0" + stt_instanceStudent  
    if instance.code == "":
        instance.code = f"{instance.year_start}{stt_instanceStudent}" 

@receiver(post_save, sender=Student)
def post_save_set_student_email(sender, instance, created, **kwargs):
    email = unidecode.name_2_email_student(ten=instance.firstname, ho=instance.lastname, dem=instance.surname, code=instance.code)
    instance.email = email

@receiver(post_save, sender=Student)
def student_send_raw_password(sender, instance, **kwargs):
    if instance.password == "":
        auto_password = Student.objects.make_random_password()
        send_raw_password(instance, auto_password)
        save_raw_password(instance, auto_password)
        instance.set_password(auto_password)
        instance.save()



#Teacher signals

@receiver(pre_save, sender=Teacher)
def pre_save_set_teacher_role(sender, instance, **kwargs):
    if instance.role != 1:
        instance.role = 1

@receiver(post_save, sender=Teacher)
def pre_save_set_teacher_email(sender, instance, **kwargs):
    email = unidecode.name_2_email_teacher(ten=instance.firstname, ho=instance.lastname, dem=instance.surname, code=None)
    
    try:
        exist_teacher = Teacher.objects.get(email=email)
    except Teacher.DoesNotExist:
        exist_teacher = None 

    code = 1

    while exist_teacher: 
        email = unidecode.name_2_email_teacher(ten=instance.firstname, ho=instance.lastname, dem=instance.surname, code=str(code))
        code = code + 1
        try:
            exist_teacher = Teacher.objects.get(email=email)
        except Teacher.DoesNotExist:
            exist_teacher = None 

    instance.email = email

@receiver(post_save, sender=Teacher)
def teacher_send_raw_password(sender, instance, created, **kwargs):
    if instance.password == "":
        auto_password = Teacher.objects.make_random_password()
        send_raw_password(instance, auto_password)
        save_raw_password(instance, auto_password)
        instance.set_password(auto_password)
        instance.save()


    




