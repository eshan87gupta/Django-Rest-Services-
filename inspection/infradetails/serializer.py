from rest_framework import serializers
from ..models import InfrastructureDetails


class InfrastructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfrastructureDetails
        fields = ('school_name', 'date', 'building', 'terrace', 'numRooms', 'enoughRooms', 'seats', 'toilet', 'cleanToilet',
                  'waterInToilet', 'approachRoad', 'roadType', 'waterSrc', 'boundary', 'ground', 'powerCon')