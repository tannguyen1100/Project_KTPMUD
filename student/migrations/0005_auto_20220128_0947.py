# Generated by Django 3.2.8 on 2022-01-28 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_student_lop_tin_chi_dang_ki'),
        ('student', '0004_alter_sinhvien_loptinchidetail_loptinchidetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinhvien_loptinchidetail',
            name='lopTinChiDetail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.lop_tin_chi_detail', verbose_name='Lớp tín chỉ'),
        ),
        migrations.CreateModel(
            name='sinhVien_dangKi_lopTinChi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=True)),
                ('lopTinChiDetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.lop_tin_chi_detail', verbose_name='Lớp tín chỉ')),
                ('sinhVien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lopTinChiĐangKi', to='users.student', verbose_name='Sinh viên')),
            ],
            options={
                'verbose_name': 'Sinh viên đăng kí lớp',
                'verbose_name_plural': 'Sinh viên đăng kí lớp',
                'unique_together': {('sinhVien', 'lopTinChiDetail')},
            },
        ),
    ]