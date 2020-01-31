from rest_framework import serializers
from ..models import surveyor_registration


class SurveyorRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = surveyor_registration
        fields = ('surveyor_name', 'surveyor_designation', 'mobile')