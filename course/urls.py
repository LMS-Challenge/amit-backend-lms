from django.urls import path, include
from .views import (
    CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView,
    CourseDeleteView, ContentCreateView, AssignmentCreateView, QuizCreateView, submit_feedback
)
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .api import CourseViewSet, ContentViewSet, AssignmentViewSet, QuizViewSet, FeedbackViewSet

router = DefaultRouter()
router.register('course', CourseViewSet, basename='course')
router.register('content', ContentViewSet, basename='content')
router.register('assignment', AssignmentViewSet, basename='assignment')
router.register('quiz', QuizViewSet, basename='quiz')
router.register('feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('api/', include(router.urls)),
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
