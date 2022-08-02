from rest_framework import serializers
from apps.accounts.models import University, Student, Sponsor, TypeSponsor
from apps.accounts.validators import phone_number, full_name


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)
    university_id = serializers.IntegerField(allow_null=False, required=True, write_only=True)

    class Meta:
        model = Student
        fields = [
            'id', 'full_name', 'phone_number', 'degree', 'contract', 'balance', 'university', 'university_id', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'balance']
        extra_kwargs = {
            'full_name': {'validators': [full_name]},
            'phone_number': {'validators': [phone_number]},
        }