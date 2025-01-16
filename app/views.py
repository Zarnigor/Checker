from rest_framework import viewsets
from .models import Submission, Problem
from app.serializers import SubmissionListSerializer, ProblemListSerializer


class SubmissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionListSerializer


class ProblemListView(viewsets.ReadOnlyModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemListSerializer
