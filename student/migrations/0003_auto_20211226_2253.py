# Generated by Django 3.2.8 on 2021-12-26 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('management', '0003_auto_20211226_2229'),
        ('student', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lop',
            name='timetable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.timetable'),
        ),
        migrations.AlterField(
            model_name='sinhvien_hocphan',
            name='hoc_phan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.hoc_phan', verbose_name='Học phần'),
        ),
        migrations.AlterField(
            model_name='sinhvien_hocphan',
            name='number',
            field=models.PositiveSmallIntegerField(verbose_name='Lần thứ'),
        ),
        migrations.AlterField(
            model_name='sinhvien_hocphan',
            name='sinh_vien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student', verbose_name='Sinh viên'),
        ),
    ]
