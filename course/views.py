from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator


from .models import course, Content, Assignment, Quiz, Feedback

# Create your views here. 


def is_instructor_or_admin(user):
    return user.is_instructor or user.is_admin


class CourseListView(generic.ListView):
    model = course
    context_object_name = 'courses'
    template_name = 'course/course_list.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for course in context['courses']:
            course.lessons_count = course.content.count()  # Assuming content has a lesson-like structure
        return context


class CourseDetailView(generic.DetailView):
    model = course
    context_object_name = 'course'
    template_name = 'course/course_detail.html'  


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_instructor_or_admin), name='dispatch')
class CourseCreateView(generic.CreateView):
    model = course
    fields = '__all__'
    template_name = 'course/course_form.html' 


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_instructor_or_admin), name='dispatch')
class CourseUpdateView(generic.UpdateView):
    model = course
    fields = ['content', 'assignments', 'quizzes', 'course_price', 'img', 'prerequisites']
    template_name = 'course/course_form.html' 


class CourseDeleteView(generic.DeleteView):
    model = course
    success_url = reverse_lazy('course_list')  # Redirect to the course list after deletion
    template_name = 'course/course_confirm_delete.html'


def submit_feedback(request, course_id):
    course_obj = get_object_or_404(course, pk=course_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        student = request.user  # Assuming the user is a Student
        Feedback.objects.create(course=course_obj, student=student, rating=rating, comment=comment)
        return redirect('course_detail', pk=course_id)  # Redirect to course detail page
    return render(request, 'course/feedback.html', {'course': course_obj})  # Specify your template name
