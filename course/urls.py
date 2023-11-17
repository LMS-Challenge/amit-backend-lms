from django.urls import path
from .views import (
    CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView,
    CourseDeleteView, ContentCreateView, AssignmentCreateView, QuizCreateView, submit_feedback
)

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('add/', CourseCreateView.as_view(), name='course_add'),
    path('<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    path('<int:pk>/content/add/', ContentCreateView.as_view(), name='content_add'),
    path('<int:pk>/assignment/add/', AssignmentCreateView.as_view(), name='assignment_add'),
    path('<int:pk>/quiz/add/', QuizCreateView.as_view(), name='quiz_add'),
    path('<int:pk>/feedback/', submit_feedback, name='submit_feedback'),
]
