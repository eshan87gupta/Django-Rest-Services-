from rest_framework import serializers
from ..models import HRTeachers


class HRTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRTeachers
        fields = ('school_name', 'date', 'teacher_name', 'teacher_designation', 'attendance', 'reason')