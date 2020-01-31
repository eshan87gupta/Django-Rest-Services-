from rest_framework import serializers
from ..models import SchoolMaster


class SchoolMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolMaster
        fields = ('school_code', 'diascode', 'school_nm_e', 'school_nm_h', 'dist_cd', 'dist_nm', 'b_cd', 'block_nm_e', 'block_nm_h', 'gp_cd', 'gp_nm_h', 'gp_nm_e', 'vill_cd', 'vill_nm_h', 'vill_nm_e', 'lat', 'lon')
