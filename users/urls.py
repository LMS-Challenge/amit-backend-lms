from django.urls import path
from .views import student_signup,login,instructor_dashboard,student_dashboard


app_name='users'
urlpatterns = [
    path('student/signup', student_signup, name='student_signup'),
    path('user/login/', login, name='login'),
    path('instructor/dashboard',instructor_dashboard, name='instructor_dashboard'),
    path('student/dashboard',student_dashboard, name='student_dashboard'),
    # Other URL patterns...
]
