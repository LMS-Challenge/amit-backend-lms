from rest_framework import serializers
from .models import CustomUser, Student, Instructor

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'is_instructor', 'is_staff', 'is_superuser']


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['title', 'name', 'gender', 'specialization', 'email', 'password', 'is_instructor', 'is_staff']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'profile_image', 'email', 'password', 'is_instructor', 'is_staff']