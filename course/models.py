from django.db import models
from django.core.validators import MaxValueValidator

from users.models import Instructor, Student

def upload_to(instance, filename):
    return 'courses/{filename}'.format(filename=filename)

def upload_to_assignments(instance, filename):
    return 'courses/{self.course_id.course_name}/{self.module_name}'.format(filename=filename)


# Create your models here.
class course(models.Model):
    course_name = models.CharField(max_length=50)
    course_description = models.TextField()
    category = models.CharField(max_length=50)
 
    instructors = models.ManyToManyField(Instructor, related_name='instructors_name')
    course_credit_hours = models.IntegerField()
    course_price = models.IntegerField()
    certificate = models.TextField(default = "", null=True, blank=True)
    img = models.ImageField(upload_to='upload_to', blank=True, null=True) #pip install pillow
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])
    prerequisites = models.ManyToManyField('self', blank=True)
    no_of_module=models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(10)])




    def __str__(self):
        return self.course_name

# class Content(models.Model):
#     module_name = models.CharField(max_length=50)
#     content_description = models.TextField()
#     content = models.FileField(upload_to='upload_to_assignments', blank=True, null=True)
#     course_id = models.ForeignKey(course, on_delete=models.CASCADE, related_name='course_content')

#     def __str__(self):
#         return self.content_name


# class Assignment(models.Model):
#     """ this class to allow student practice by solve assignments number of assignments is the same as number of modules in courses"""
#     students = models.ManyToManyField(Student, related_name='instructors_name')
#     course = models.ForeignKey(course, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     explain_assignments = models.TextField()
#     due_date = models.DateTimeField()

#     def __str__(self):
#         return self.title


# class Quiz(models.Model):
#     course = models.ForeignKey(course, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     questions = models.ManyToManyField('Question')

#     def __str__(self):
#         return self.title

# class Question(models.Model):
#     text = models.TextField()
#     options = models.JSONField()  # Store options as a JSON array
#     correct_answer = models.PositiveIntegerField()

#     def __str__(self):
#         return self.text
