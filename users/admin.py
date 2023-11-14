from django.contrib import admin

from users.models import Instructor, Student

# Register your models here.
admin.site.register(Instructor)
admin.site.register(Student)


