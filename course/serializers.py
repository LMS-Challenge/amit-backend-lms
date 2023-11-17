from rest_framework import serializers
from .models import course, Content, Assignment, Quiz, Feedback
from users.models import Instructor, Student

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['email', 'name', 'title', 'gender', 'specialization']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'gender']

class CourseSerializer(serializers.ModelSerializer):
    instructors = InstructorSerializer(many=True, read_only=True)
    
    class Meta:
        model = course
        fields = [
            'id', 'course_name', 'course_description', 'category',
            'instructors', 'course_credit_hours', 'course_price',
            'certificate', 'course_image', 'rating',
        ]

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'course', 'content', 'content_description']

class AssignmentSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Assignment
        fields = ['id', 'course', 'title', 'explain_assignments', 'assignment_file', 'students', 'due_date']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'course', 'quiz_title', 'quiz_deadline']

class FeedbackSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    
    class Meta:
        model = Feedback
        fields = ['id', 'course', 'student', 'rating', 'comment']
