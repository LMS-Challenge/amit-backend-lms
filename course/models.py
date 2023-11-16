from django.db import models
from django.core.validators import MaxValueValidator

from users.models import Instructor, Student

def upload_to(instance, filename):
    return 'course/{filename}'.format(filename=filename)


CATEGORIES = [
    'Development',
    'Business',
    'IT_and_Software',
    'Data & Machine Learning',
    'Design',
    'Marketing',
    'Cloud & DevOps',
    'Cybersecurity',
    'Life Skills',
]


# Create your models here.
class course(models.Model):
    course_name = models.CharField(max_length=50)
    course_description = models.TextField()
    category = models.CharField(max_length=50)
    content = models.ManyToManyField('Content', related_name='course_content')
    assignments = models.ManyToManyField('Assignment', related_name='course_assignment')
    quizzes = models.ManyToManyField('Quiz', related_name='course_quiz')
    instructors = models.ManyToManyField(Instructor, related_name='instructors_name')
    course_credit_hours = models.IntegerField()
    course_price = models.IntegerField()
    certificate = models.TextField(default = "", null=True, blank=True)
    img = models.ImageField(upload_to='course', blank=True, null=True) #pip install pillow
    prerequisites = models.ManyToManyField('self', blank=True)


    def __str__(self):
        return self.course_name


class Content(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='course_content')
    content_type = models.CharField(max_length=50) #video, pdf, text
    file = models.FileField(upload_to='content_files/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.description
    
class Assignment(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='course_assignment')
    assignment_name = models.CharField(max_length=50)
    assignment_description = models.TextField()
    assignment_file = models.FileField(upload_to='assignment_files/', blank=True, null=True)
    assignment_deadline = models.DateTimeField()

    def __str__(self):
        return self.assignment_name
    
class Quiz(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='course_quiz')
    quiz_name = models.CharField(max_length=50)
    quiz_description = models.TextField()
    quiz_deadline = models.DateTimeField()

    def __str__(self):
        return self.quiz_name


class Feedback(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='feedback')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5)])
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Feedback for {self.course.course_name} by {self.student}"