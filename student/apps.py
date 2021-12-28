from django.apps import AppConfig


class StudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student'
    verbose_name = "Sinh viên"

    def ready(self):
        import student.signals