from rest_framework.serializers import ModelSerializer
from app.models import Submission, Problem


class SubmissionListSerializer(ModelSerializer):
    class Meta:
        model = Submission
        exclude = ('source_code',)

class SubmissionUserListSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

class ProblemListSerializer(ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'
