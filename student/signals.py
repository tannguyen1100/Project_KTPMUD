from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from student.models import lop, sinhvien_hocphan

@receiver(pre_save, sender=lop)
def post_save_create_bang_diem(sender, instance, **kwargs):

    sinhVienList = instance.sinh_vien.all()
    hocPhan = instance.hoc_phan
    lop = instance

    print(sinhVienList)
    print(hocPhan)
    print(lop)
    # for sinhVien in sinhVienList:

    # update_values = {"is_manager": False}
    # new_values = {"name": "Bob", "age": 25, "is_manager":True}

    # bang_diem, created = sinhvien_hocphan.objects.update_or_create(identifier='id', defaults=update_values)

    # if created:
    #     bang_diem.update(**new_values)