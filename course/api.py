from rest_framework import viewsets
from .models import course, Content, Assignment, Quiz, Feedback
from .serializers import (
    CourseSerializer, ContentSerializer, AssignmentSerializer,
    QuizSerializer, FeedbackSerializer
)
from drf_spectacular.utils import extend_schema

class CourseViewSet(viewsets.ModelViewSet):
    queryset = course.objects.all()
    serializer_class = CourseSerializer

    @extend_schema(tags=['course'])
    def get_queryset(self):
        return course.objects.all()

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    @extend_schema(tags=['content'])
    def get_queryset(self):
        return Content.objects.all()

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    @extend_schema(tags=['assignment'])
    def get_queryset(self):
        return Assignment.objects.all()

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    @extend_schema(tags=['quiz'])
    def get_queryset(self):
        return Quiz.objects.all()

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    @extend_schema(tags=['feedback'])
    def get_queryset(self):
        return Feedback.objects.all()
