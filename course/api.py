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

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
