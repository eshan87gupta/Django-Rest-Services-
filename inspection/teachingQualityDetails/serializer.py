from rest_framework import serializers
from ..models import TeachingQuality


class TeachingQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingQuality
        fields = ('school_name', 'date', 'standard', 'syll_status', 'lang_level', 'math_level', 'gen_level')