from rest_framework import serializers
from ..models import MDMData


class MDMDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MDMData
        fields = ('school_name', 'date', 'agencyName', 'numMem', 'presName', 'secName')