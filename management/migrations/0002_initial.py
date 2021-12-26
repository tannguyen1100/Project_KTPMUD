# Generated by Django 3.2.8 on 2021-12-25 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vien_dao_tao',
            name='vien_truong',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vien_quan_ly', to='users.teacher', verbose_name='Viện trưởng'),
        ),
        migrations.AddField(
            model_name='lop_chung',
            name='giao_vien',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cac_lop_quan_ly', to='users.teacher', verbose_name='Giáo viên quản lý'),
        ),
        migrations.AddField(
            model_name='lop_chung',
            name='khoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lop_cung_khoa', to='management.khoa'),
        ),
        migrations.AddField(
            model_name='lop_chung',
            name='vien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cac_lop_thuoc_vien', to='management.vien_dao_tao', verbose_name='Viện quản lý'),
        ),
        migrations.AddField(
            model_name='hoc_phan',
            name='vien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cac_hoc_phan', to='management.vien_dao_tao', verbose_name='Viện trực thuộc'),
        ),
    ]
