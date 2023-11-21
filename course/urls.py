from django.urls import path, include
from .views import (
    CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView,
    ContentListView, ContentDetailView, ContentCreateView, ContentUpdateView, ContentDeleteView,
    AssignmentListView, AssignmentDetailView, AssignmentCreateView, AssignmentUpdateView, AssignmentDeleteView,
    QuizListView, QuizDetailView, QuizCreateView, QuizUpdateView, QuizDeleteView,
    submit_feedback
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

    ##################################Course URLS######################################
    path('', CourseListView.as_view(), name='course_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('add/', CourseCreateView.as_view(), name='course_add'),
    path('<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),

    ##################################Content URLS######################################
    path('<int:pk>/content/', ContentListView.as_view(), name='content_list'),
    path('<int:pk>/content/detail/', ContentDetailView.as_view(), name='content_detail'),
    path('<int:pk>/content/add/', ContentCreateView.as_view(), name='content_add'),
    path('<int:pk>/content/update/', ContentUpdateView.as_view(), name='content_update'),
    path('<int:pk>/content/delete/', ContentDeleteView.as_view(), name='content_delete'),

    ##################################Assignment URLS######################################
    path('<int:pk>/assignment/', AssignmentListView.as_view(), name='assignment_list'),
    path('<int:pk>/assignment/detail/', AssignmentDetailView.as_view(), name='assignment_detail'),
    path('<int:pk>/assignment/add/', AssignmentCreateView.as_view(), name='assignment_add'),
    path('<int:pk>/assignment/update/', AssignmentUpdateView.as_view(), name='assignment_update'),
    path('<int:pk>/assignment/delete/', AssignmentDeleteView.as_view(), name='assignment_delete'),

    ##################################Quiz URLS######################################
    path('<int:pk>/quiz/', QuizListView.as_view(), name='quiz_list'),
    path('<int:pk>/quiz/detail/', QuizDetailView.as_view(), name='quiz_detail'),
    path('<int:pk>/quiz/add/', QuizCreateView.as_view(), name='quiz_add'),
    path('<int:course_pk>/quiz/<int:pk>/update/', QuizUpdateView.as_view(), name='quiz_update'),
    path('<int:course_pk>/quiz/<int:pk>/delete/', QuizDeleteView.as_view(), name='quiz_delete'),

    ##################################Feedback URLS######################################
    path('<int:pk>/feedback/', submit_feedback, name='submit_feedback'),
]
