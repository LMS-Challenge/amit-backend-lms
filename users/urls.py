from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .api import CustomUserViewSet, StudentViewSet, InstructorViewSet
from .views import student_signup,custom_login,instructor_dashboard,student_dashboard


router = DefaultRouter()
router.register('users', CustomUserViewSet)
router.register('students', StudentViewSet)
router.register('instructors', InstructorViewSet)

app_name='users'
urlpatterns = [
    path('api/', include(router.urls)),
    path('signup', student_signup, name='student-signup'),
    path('', custom_login, name='login'),
    path('instructor/dashboard',instructor_dashboard, name='instructor_dashboard'),
    path('student/dashboard',student_dashboard, name='student_dashboard'),
    
]
