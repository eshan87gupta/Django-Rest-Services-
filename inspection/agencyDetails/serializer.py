from rest_framework import serializers
from ..models import MDMDataDetails


class AgencyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MDMDataDetails
        fields = ('sn', 'dCode', 'schName', 'devBlk', 'agencyName')