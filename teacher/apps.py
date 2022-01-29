from django.apps import AppConfig


class TeacherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teacher'
    verbose_name = "3. Giáo viên"

    def ready(self):
        import teacher.signals