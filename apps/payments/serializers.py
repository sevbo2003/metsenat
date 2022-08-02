from rest_framework import serializers
from apps.accounts.serializers import StudentSerializer, SponsorSerializer
from apps.payments.models import Sponsorship
from apps.payments.validators import validate_payment, update_payment


class SponsorshipSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    sponsor = SponsorSerializer(read_only=True)

    student_id = serializers.IntegerField(required=True, write_only=True)
    sponsor_id = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        model = Sponsorship
        fields = [
            'id', 'sponsor', 'student', 'id', 'sponsor_id', 'student_id', 'amount'
        ]

    def create(self, validated_data):
        data = validate_payment(validated_data=validated_data)
        return data

    def update(self, instance, validated_data):
        instance = update_payment(instance, validated_data)
        return instance