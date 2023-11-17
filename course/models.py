from django.db import models
from django.core.validators import MaxValueValidator

from users.models import Instructor, Student

def upload_to(instance, filename):
    return 'course/{course_id}/{filename}'.format(filename=filename)

# def upload_to_assignments(instance, filename):
#     return 'course/{self.course_id.course_name}/{self.module_name}'.format(filename=filename)



CATEGORY_CHOICES = [
        ('development', 'Development'),
        ('business', 'Business'),
        ('it_and_software', 'IT and Software'),
        ('data_machine_learning', 'Data & Machine Learning'),
        ('design', 'Design'),
        ('marketing', 'Marketing'),
        ('cloud_devops', 'Cloud & DevOps'),
        ('cybersecurity', 'Cybersecurity'),
        ('life_skills', 'Life Skills'),
    ]

CERTIFICATE_CHOICES = [
    ('completion', 'Upon Completion'),
    ('none', 'No Certificate'),
]


# Create your models here.
class course(models.Model):
    course_name = models.CharField(max_length=50)
    course_description = models.TextField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='development',
    )
    instructors = models.ManyToManyField(Instructor, related_name='instructors_name')
    course_credit_hours = models.IntegerField()
    course_price = models.IntegerField()
    certificate = models.CharField(
        max_length=50,
        choices=CERTIFICATE_CHOICES,
        default='none',
        blank=True,
        null=True
    )
    course_image = models.ImageField(upload_to=upload_to, blank=True, null=True) #pip install pillow
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])
    # prerequisites = models.ManyToManyField('self', blank=True)
    # no_of_module=models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(10)])


    def __str__(self):
        return self.course_name


class Content(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='course_content')
    content = models.FileField(upload_to='content/', blank=True, null=True)
    content_description = models.TextField()

    def __str__(self):
        return self.content_description
    

class Assignment(models.Model):
    """ this class to allow student practice by solve assignments number of assignments is the same as number of modules in courses"""
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    explain_assignments = models.TextField()
    assignment_file = models.FileField(upload_to=upload_to, blank=True, null=True)
    students = models.ManyToManyField(Student, related_name='student_assignments')
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title
    

class Quiz(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='course_quiz')
    quiz_title = models.CharField(max_length=50)
    quiz_deadline = models.DateTimeField()
    #questions = models.ManyToManyField('Question')

    def __str__(self):
        return self.quiz_title


# class Question(models.Model):
#     text = models.TextField()
#     options = models.JSONField()  # Store options as a JSON array
#     correct_answer = models.PositiveIntegerField()

#     def __str__(self):
#         return self.text


class Feedback(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='feedback')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5)])
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Feedback for {self.course.course_name} by {self.student}"




