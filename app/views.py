from rest_framework import viewsets
from .models import Submission, Problem
from app.serializers import SubmissionListSerializer, ProblemListSerializer, SubmissionUserListSerializer


class SubmissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Submission.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return SubmissionListSerializer
        return SubmissionUserListSerializer


class ProblemListView(viewsets.ReadOnlyModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemListSerializer
