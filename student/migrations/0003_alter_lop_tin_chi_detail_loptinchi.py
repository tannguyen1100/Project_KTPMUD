# Generated by Django 3.2.8 on 2022-01-27 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20220127_2307'),
        ('student', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lop_tin_chi_detail',
            name='lopTinChi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='management.lop_tin_chi', verbose_name='Lớp tín chỉ'),
        ),
    ]