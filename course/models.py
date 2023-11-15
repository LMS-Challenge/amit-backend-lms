from django.db import models
from django.core.validators import MaxValueValidator

from users.models import Instructor, Student

def upload_to(instance, filename):
    return 'course/{filename}'.format(filename=filename)

# Create your models here.
class course(models.Model):
    course_name = models.CharField(max_length=50)
    course_description = models.TextField()
    category = models.CharField(max_length=50)
    # content = models.ManyToManyField('Content')
    # assignments = models.ManyToManyField('Assignment')
    # quizzes = models.ManyToManyField('Quiz')
    instructors = models.ManyToManyField(Instructor, related_name='instructors_name')
    course_credit_hours = models.IntegerField()
    course_price = models.IntegerField()
    certificate = models.TextField(default = "", null=True, blank=True)
    img = models.ImageField(upload_to='course', blank=True, null=True) #pip install pillow
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])
    prerequisites = models.ManyToManyField('self', blank=True)




    def __str__(self):
        return self.course_name

# class Content(models.Model):
#     content_name = models.CharField(max_length=50)
#     content_description = models.TextField()
#     content = models.FileField(upload_to='content', blank=True, null=True)
#     course_id = models.ForeignKey(course, on_delete=models.CASCADE, related_name='course_content')

#     def __str__(self):
#         return self.content_name
    