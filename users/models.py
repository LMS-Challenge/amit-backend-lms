from django.db import models
from django.contrib.auth.models import AbstractUser


def upload_to(instance, filename):
    return 'course/{filename}'.format(filename=filename)


GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ]


# Create your models here.
class CustomUser(AbstractUser):
    is_instructor = models.BooleanField(default=False)

class Instructor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='instructor')
    title = models.CharField(max_length=10, default='Dr.')
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    specialization = models.CharField(max_length=50)


    def save(self, *args, **kwargs):
        # Set is_instructor to True for the user
        if not self.user.is_instructor:
            self.user.is_instructor = True
            self.user.save()

        super(Instructor, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} {self.name}"

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    # profile_image = models.ImageField(upload_to=upload_to, blank=True, null=True) #pip install pillow


    def __str__(self):
        return f"{self.first_name} {self.last_name}"