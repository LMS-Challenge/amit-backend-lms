from django.contrib import admin

from users.models import Instructor, Student,CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_instructor',)


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'specialization',)
    list_filter = ('specialization',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth' ,'gender',)
    list_filter = ('gender',)