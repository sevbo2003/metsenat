from django.shortcuts import get_object_or_404
from apps.accounts.models import Student, Sponsor
from apps.payments.models import Sponsorship
from rest_framework.validators import ValidationError
from django.db.models import Sum
from django.db.models.functions import Coalesce


def validate_payment(validated_data):
    student = get_object_or_404(Student, id=validated_data["student_id"])
    sponsor = get_object_or_404(Sponsor, id=validated_data["sponsor_id"])
    money = validated_data["amount"]

    if money <= sponsor.balance:
        if student.balance + money <= student.contract:
            sponsorship = Sponsorship.objects.create(**validated_data)

            sponsor2 = Sponsor.objects.get(id=sponsor.id)
            sponsor2.balance = sponsor2.balance - money
            sponsor2.sponsored = sponsor2.sponsored + money
            student2 = Student.objects.get(id=student.id)
            student2.balance = student2.balance + money
            sponsor2.save()
            student2.save()

            return sponsorship
        else:
            raise ValidationError(
                {"pull yetmadi": "Homiylik summasi kontrakt summasidan oshib ketdi."}
            )
    else:
        raise ValidationError(
            {
                "pull yetmadi": f"Homiy balansida {money} sum pul mavjud emas."
            }
        )


def update_payment(data, validate_data):
    student = get_object_or_404(Student, id=validate_data["student_id"])
    sponsor = get_object_or_404(Sponsor, id=validate_data["sponsor_id"])
    money = validate_data["amount"]

    if money <= sponsor.balance:
        if student.balance + money <= student.contract:
            data.money = money
            data.sponsor = sponsor
            data.save()
            return data
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