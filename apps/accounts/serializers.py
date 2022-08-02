from rest_framework import serializers
from apps.accounts.models import University, Student, Sponsor, TypeSponsor


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'