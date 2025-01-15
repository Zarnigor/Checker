from django.shortcuts import render

from rest_framework import viewsets
from .models import Submission
from app.serializers import SubmissionListSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionListSerializer
