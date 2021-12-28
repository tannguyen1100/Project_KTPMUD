# Generated by Django 3.2.8 on 2021-12-26 15:22

from django.db import migrations, models
import django.db.models.deletion
import student.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('type', models.CharField(choices=[('Lý thuyết', 'LT'), ('Thí nghiệm', 'TN')], default='Lý thuyết', max_length=20, verbose_name='Loại lớp')),
            ],
            options={
                'verbose_name': 'Lớp tín chỉ',
                'verbose_name_plural': 'Lớp tín chỉ',
            },
        ),
        migrations.CreateModel(
            name='week',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Tuần')),
            ],
            options={
                'verbose_name': 'Tuần',
                'verbose_name_plural': 'Tuần',
            },
        ),
        migrations.CreateModel(
            name='timing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.TimeField(verbose_name='Thời gian bắt đầu')),
                ('time_end', models.TimeField(verbose_name='Thời gian kết thúc')),
            ],
            options={
                'verbose_name': 'Thời gian',
                'verbose_name_plural': 'Thời gian',
                'unique_together': {('time_start', 'time_end')},
            },
        ),
        migrations.CreateModel(
            name='timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=15)),
                ('week', models.ManyToManyField(to='student.week')),
            ],
            options={
                'verbose_name': 'Thời khóa biểu',
                'verbose_name_plural': 'Thời khóa biểu',
            },
        ),
        migrations.CreateModel(
            name='sinhvien_hocphan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('giua_ki', models.FloatField(blank=True, null=True, validators=[student.validators.validate_score], verbose_name='Điểm giữa kì')),
                ('cuoi_ki', models.FloatField(blank=True, null=True, validators=[student.validators.validate_score], verbose_name='Điểm cuối kì')),
                ('hoc_phan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.hoc_phan')),
            ],
            options={
                'verbose_name': 'Bảng điểm',
                'verbose_name_plural': 'Bảng điểm',
            },
        ),
    ]