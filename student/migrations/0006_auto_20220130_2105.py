# Generated by Django 3.2.8 on 2022-01-30 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_alter_semester_name'),
        ('student', '0005_auto_20220128_0947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sinhvien_dangki_loptinchi',
            options={'verbose_name': 'Sinh viên đăng kí lớp tín chỉ', 'verbose_name_plural': 'Sinh viên đăng kí lớp tín chỉ'},
        ),
        migrations.AlterUniqueTogether(
            name='lop_tin_chi_detail',
            unique_together={('lopTinChi', 'semester')},
        ),
    ]
