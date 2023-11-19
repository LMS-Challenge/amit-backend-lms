from django.contrib import admin
from .models import course, Content, Assignment, Quiz

# Register your models here.
@admin.register(course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'category', 'course_price', 'certificate', 'rating',)
    list_filter = ('category', 'course_price' ,'certificate', 'rating',)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('course', 'content', 'content_description',)


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'due_date',)
    list_filter = ('due_date',)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('course', 'quiz_title','quiz_deadline',)
    list_filter = ('quiz_deadline',)
