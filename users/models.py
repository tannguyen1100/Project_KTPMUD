from os import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
from management.models import vien_dao_tao, lop_chung, khoa

import datetime

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, password=None,is_superuser=False, is_active=True, **extra_fields):
        if not email:
            raise ValueError('Email requied')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_superuser=is_superuser,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

 
class User(AbstractBaseUser, PermissionsMixin):
    class Genders(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"

    avatar = models.ImageField(_("Ảnh đại diện"), upload_to="Avatar", blank=True, null=True)
    email = models.EmailField(_("Email"),max_length=50, unique=True, blank=True)
    firstname = models.CharField(_("Tên"),max_length=20,  blank=False, null=True)
    surname = models.CharField(_("Tên đệm"),max_length=20, null=True, blank=True)
    lastname = models.CharField(_("Họ"),max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(_("Ngày sinh"), blank=True, null=True, )
    phone = models.CharField(_("Số điện thoại"), max_length=15, blank=True, null=True)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    role = models.BooleanField(null=True, blank=True)

    gender = models.CharField(
        _("Gender"), max_length=50, choices=Genders.choices, default=Genders.MALE
    ) 

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.is_superuser  


class Student(User):
    year_start = models.IntegerField(_("Năm vào trường"), default=datetime.datetime.now().year)
    vien = models.ForeignKey(vien_dao_tao, verbose_name="Viện", on_delete=models.CASCADE, null=True, blank=True)
    lop_chung = models.ForeignKey(lop_chung,verbose_name="Lớp chung", on_delete=models.CASCADE, related_name="sinh_vien", null=True, blank=True)
    code = models.CharField(_("Mã số sinh viên"), max_length=8, blank=True, unique=True)
    khoa = models.ForeignKey(khoa, verbose_name="Khóa" , max_length=3, blank=True, on_delete=CASCADE, null=True)

    lop_tin_chi_dang_ki = models.ManyToManyField('student.lop_tin_chi_detail', verbose_name="Lớp tín chỉ đăng kí", related_name='sinh_vien_trong_lop_tin_chi')

    def __str__(self):
        return self.email.replace("@edu.com.vn", "")
    
    def getfullname(self):
        if self.lastname:
            if self.surname:
                return f"{self.lastname} {self.surname} {self.firstname}"
            else:
                return f"{self.lastname} {self.firstname}"
        else:
            return f"{self.firstname}"
    class Meta:
        verbose_name = "Sinh viên"
        verbose_name_plural = 'Sinh viên'


class Teacher(User):
    year_start = models.IntegerField(_("Năm bắt đầu công tác"), default=2015)
    vien = models.ForeignKey('management.vien_dao_tao', on_delete=models.CASCADE, verbose_name="Viện",related_name="cac_giao_vien", null=True,blank=True)

    chuyen_mon = models.ManyToManyField('management.hoc_phan', verbose_name="Học phần", related_name='giao_vien_theo_chuyen_mon')


    def __str__(self):
        return f"{self.email}"

    def getfullname(self):
        if self.lastname:
            if self.surname:
                return f"{self.lastname} {self.surname} {self.firstname}"
            else:
                return f"{self.lastname} {self.firstname}"
        else:
            return f"{self.firstname}"

    class Meta:
        verbose_name = "Giáo viên"
        verbose_name_plural = 'Giáo viên'


