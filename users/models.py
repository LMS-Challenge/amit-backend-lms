from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


def upload_to(instance, filename):
    return 'students/{filename}'.format(filename=filename)

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

class CustomUserManager(BaseUserManager):
    
    # It provides methods for creating users and superusers.
    
    def create_user(self, email, password=None, **extra_fields):
        
        # method creates a regular user with the given email and password.
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # method creates a superuser (admin) with the given email and password.
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # It represents our custom user model with basic fields.
    
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    objects = CustomUserManager()
    
    # specifies the field to use as the unique identifier (in this case, it’s the email).
    USERNAME_FIELD = 'email'
    # ists any additional fields required when creating a user.
    REQUIRED_FIELDS = []

from django.contrib.auth.hashers import make_password

class Instructor(CustomUser):
    
  
    title = models.CharField(max_length=10, default='Dr.')
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    specialization = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        """The save method ensures that the associated user’s is_instructor and is_staff fields are set correctly.
         and override the default one in customuser"""
        # Set is_instructor to True for the user
        if not self.is_instructor:
            self.is_instructor = True
            self.is_staff = True  # Set is_staff to True for instructors

        # Hash the password before saving
        self.password = make_password(self.password)

        super(Instructor, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} {self.name}"


class Student(CustomUser):
    # This model represents students.
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    profile_image = models.ImageField(upload_to=upload_to, blank=True, null=True) 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def get_object_or_none(cls, **kwargs):
        try:
            return Student.objects.get(**kwargs)

        except Student.DoesNotExist:
            return None
