from rest_framework import viewsets
from .models import Submission, Problem
from app.serializers import SubmissionListSerializer, ProblemListSerializer


class SubmissionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SubmissionListSerializer

    def get_queryset(self):
        user = self.request.user
        return Submission.objects.filter(user=user)


class ProblemListView(viewsets.ReadOnlyModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemListSerializer
