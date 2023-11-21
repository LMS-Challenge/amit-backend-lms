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

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.object.pk})


class CourseDeleteView(generic.DeleteView):
    model = course
    template_name = 'course/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')



class ContentListView(generic.ListView):
    model = Content
    context_object_name = 'contents'
    template_name = 'course/content_list.html'

    def get_queryset(self):
        return Content.objects.filter(course=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = get_object_or_404(course, pk=self.kwargs['pk'])
        return context


class ContentDetailView(generic.DetailView):
    model = Content
    context_object_name = 'content'
    template_name = 'course/content_detail.html'


class ContentCreateView(generic.CreateView):
    model = Content
    fields = ['content', 'content_description']
    template_name = 'course/content_form.html'
    success_url = reverse_lazy('course_detail')


class ContentUpdateView(generic.UpdateView):
    model = Content
    fields = ['content', 'content_description']
    template_name = 'course/content_form.html'
    success_url = reverse_lazy('course_detail')


class ContentDeleteView(generic.DeleteView):
    model = Content
    template_name = 'course/content_confirm_delete.html'
    success_url = reverse_lazy('content_list')



class AssignmentListView(generic.ListView):
    model = Assignment
    context_object_name = 'assignments'
    template_name = 'course/assignment_list.html'

    def get_queryset(self):
        return self.model.objects.filter(course_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = get_object_or_404(course, pk=self.kwargs['pk'])
        return context


class AssignmentDetailView(generic.DetailView):
    model = Assignment
    context_object_name = 'assignment'
    template_name = 'course/assignment_detail.html'


class AssignmentCreateView(generic.CreateView):
    model = Assignment
    fields = ['title', 'explain_assignments', 'assignment_file', 'due_date']
    template_name = 'course/assignment_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'pk' in self.kwargs:
            context['course'] = get_object_or_404(course, pk=self.kwargs['pk'])
        return context


    def form_valid(self, form):
        form.instance.course = get_object_or_404(course, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('assignment_list', kwargs={'pk': self.object.course.pk})


class AssignmentUpdateView(generic.UpdateView):
    model = Assignment
    fields = ['title', 'explain_assignments', 'assignment_file', 'due_date']
    template_name = 'course/assignment_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ensure that 'pk' keyword argument is present in the URLconf
        if 'pk' in self.kwargs:
            # Get the course object to pass to the template
            context['course'] = get_object_or_404(Assignment, pk=self.kwargs['pk']).course
        return context

    def get_success_url(self):
        # Assuming that an assignment has a 'course' ForeignKey to redirect to its detail
        return reverse_lazy('assignment_list', kwargs={'pk': self.object.course.pk})


class AssignmentDeleteView(generic.DeleteView):
    model = Assignment
    template_name = 'course/assignment_confirm_delete.html'
    course_pk = None

    def get_object(self, queryset=None):
        obj = super(AssignmentDeleteView, self).get_object(queryset)
        self.course_pk = obj.course.pk
        return obj

    def get_success_url(self):
        if self.course_pk:
            return reverse_lazy('assignment_list', kwargs={'pk': self.course_pk})
        else:
            return reverse_lazy('course_list')


class QuizListView(generic.ListView):
    model = Quiz
    context_object_name = 'quizzes'
    template_name = 'course/quiz_list.html'

    def get_queryset(self):
        return Quiz.objects.filter(course=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = get_object_or_404(course, pk=self.kwargs['pk'])
        return context


class QuizDetailView(generic.DetailView):
        model = Quiz
        context_object_name = 'quiz'
        template_name = 'course/quiz_detail.html'


class QuizCreateView(generic.CreateView):
    model = Quiz
    fields = ['quiz_title', 'quiz_deadline']
    template_name = 'course/quiz_form.html'

    def get_context_data(self, **kwargs):
        context = super(QuizCreateView, self).get_context_data(**kwargs)
        # Assuming the course's pk is passed via URL as 'pk' or 'course_pk'
        context['course'] = get_object_or_404(course, pk=self.kwargs.get('pk') or self.kwargs.get('course_pk'))
        return context

    def form_valid(self, form):
        # Assuming that you have a ForeignKey in Quiz model pointing to Course as 'course'
        form.instance.course = get_object_or_404(course, pk=self.kwargs.get('pk') or self.kwargs.get('course_pk'))
        return super(QuizCreateView, self).form_valid(form)

    def get_success_url(self):
        # Redirect to the quiz list for the course
        return reverse_lazy('quiz_list', kwargs={'pk': self.object.course.pk})


class QuizUpdateView(generic.UpdateView):
    model = Quiz
    fields = ['quiz_title', 'quiz_deadline']
    template_name = 'course/quiz_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.object.course
        return context

    def get_success_url(self):
        return reverse_lazy('quiz_list', kwargs={'pk': self.object.course.pk})


class QuizDeleteView(generic.DeleteView):
    model = Quiz
    template_name = 'course/quiz_confirm_delete.html'
    success_url = reverse_lazy('quiz_list')


def submit_feedback(request, pk):
    course_obj = get_object_or_404(course, pk=pk)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        student = request.user  # Assuming the user is a Student
        Feedback.objects.create(course=course_obj, student=student, rating=rating, comment=comment)
        return redirect('course_detail', pk=pk)  # Redirect to course detail page
    return render(request, 'course/feedback.html', {'course': course_obj})  # Specify your template name

