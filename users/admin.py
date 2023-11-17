from django.contrib import admin

from users.models import Instructor, Student,CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Instructor)
admin.site.register(Student)



# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ["email", "username",]

# admin.site.register(CustomUser, CustomUserAdmin)
