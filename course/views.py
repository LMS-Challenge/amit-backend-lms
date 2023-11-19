from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.db.models import Count


from .models import course, Content, Assignment, Quiz, Feedback

# Create your views here.

def is_instructor_or_superuser(user):
    return user.is_instructor or user.is_superuser


class CourseListView(generic.ListView):
    model = course
    context_object_name = 'courses'
    template_name = 'course_list.html'

    def get_queryset(self):
        # Use annotate to efficiently count the content for each course
        return course.objects.annotate(lessons_count=Count('course_content'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # The lessons_count is now part of each course object, no need to iterate
        return context



class CourseDetailView(generic.DetailView):
    model = course
    context_object_name = 'course'
    template_name = 'course/course_detail.html'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_instructor_or_superuser), name='dispatch')
class CourseCreateView(generic.CreateView):
    model = course
    fields = ['course_name', 'course_image', 'course_description', 'category', 'course_credit_hours', 'course_price', 'certificate', 'rating']
    template_name = 'course/course_form.html'
    success_url = reverse_lazy('course_list')



@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_instructor_or_superuser), name='dispatch')
class CourseUpdateView(generic.UpdateView):
    model = course
    fields = ['course_description', 'instructors','course_price', 'rating']
    template_name = 'course/course_form.html'
    success_url = reverse_lazy('course_detail')


class CourseDeleteView(generic.DeleteView):
    model = course
    success_url = reverse_lazy('course_list')  # Redirect to the course list after deletion
    template_name = 'course/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')


class ContentCreateView(generic.CreateView):
    model = Content
    fields = ['content', 'content_description']
    template_name = 'course/content_form.html'
    success_url = reverse_lazy('course_detail')


class AssignmentCreateView(generic.CreateView):
    model = Assignment
    fields = ['title', 'explain_assignments', 'assignment_file', 'due_date']
    template_name = 'course/assignment_form.html'
    success_url = reverse_lazy('course_detail')


class QuizCreateView(generic.CreateView):
    model = Quiz
    fields = ['quiz_title', 'quiz_deadline']
    template_name = 'course/quiz_form.html'
    success_url = reverse_lazy('course_detail')


def submit_feedback(request, pk):
    course_obj = get_object_or_404(course, pk=pk)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        student = request.user  # Assuming the user is a Student
        Feedback.objects.create(course=course_obj, student=student, rating=rating, comment=comment)
        return redirect('course_detail', pk=pk)  # Redirect to course detail page
    return render(request, 'course/feedback.html', {'course': course_obj})  # Specify your template name

