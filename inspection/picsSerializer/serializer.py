from rest_framework import serializers
from ..models import SchoolSelfies


class SchoolSelfiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolSelfies
        fields = ('sch_selfie',)
