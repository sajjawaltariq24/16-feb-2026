from rest_framework import serializers
from .models import Organize, Practice, Patient

class OrganizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organize
        fields = '_all_'

class PracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practice
        fields = '_all_'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '_all_'