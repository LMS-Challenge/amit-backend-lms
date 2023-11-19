from django.db import models
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError

from users.models import Student
from course.models import course

# Create your models here.
class offer(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='course_offer')
    description = models.TextField()
    enrolled_students = models.ManyToManyField(Student, related_name='enrolled_students')
    max_capacity = models.PositiveIntegerField()
    current_enrollment = models.PositiveIntegerField(default=0)
    waiting_list = models.ManyToManyField(Student, related_name='waiting_list_offers', blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    new_price = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(default=0)
    duration = models.DurationField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Expired', 'Expired'), ('Upcoming', 'Upcoming')], default='active')

    def clean(self):
        # Ensure the course is set before checking its price
        if not self.course:
            raise ValidationError({'course': "Course must be set to validate discount."})
        # Set the maximum discount to be the course price
        max_discount = self.course.course_price
        if self.discount > max_discount:
            raise ValidationError({'discount': f"Discount cannot be greater than the course price (${max_discount})."})

    def __str__(self):
        return f"{self.course.course_name}'s Offer is available from {self.start_date} To {self.end_date}"
