from rest_framework import serializers
from apps.accounts.serializers import StudentSerializer, SponsorSerializer
from apps.accounts.models import Student, Sponsor
from apps.payments.models import Sponsorship
from apps.payments.validators import validate_payment, update_payment
from django.shortcuts import get_object_or_404
from rest_framework.validators import ValidationError


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
        student = get_object_or_404(Student, id=instance.student_id)
        sponsor = get_object_or_404(Sponsor, id=instance.sponsor_id)
        money = validated_data.get("amount", instance.amount)

        if money <= sponsor.balance:
            if student.balance + money <= student.contract:
                instance.amount = money
                sponsor.balance = sponsor.balance - money
                sponsor.sponsored = sponsor.sponsored + money
                student.balance = student.balance + money
                sponsor.save()
                student.save()
                instance.save()
                return instance
            else:
                raise ValidationError(
                    {"pull yetmadi": "Homiylik puli kontrakt pulidan oshib ketdi."}
                )
        else:
            raise ValidationError(
                {
                    "pull yetmadi": f"Homiy balansida {money} sum pul mavjud emas."
                }
            )