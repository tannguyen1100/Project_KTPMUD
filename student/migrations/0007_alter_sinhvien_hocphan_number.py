# Generated by Django 3.2.8 on 2021-12-28 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_lop_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinhvien_hocphan',
            name='number',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Lần thứ'),
        ),
    ]
