from rest_framework.serializers import ModelSerializer

from app.models import Submission


class SubmissionListSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
