# Generated by Django 3.2.8 on 2021-12-28 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_student_lop'),
        ('management', '0003_auto_20211226_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoc_phan',
            name='sinh_vien',
            field=models.ManyToManyField(blank=True, related_name='hocPhan', to='users.Student', verbose_name='Sinh viên'),
        ),
    ]
