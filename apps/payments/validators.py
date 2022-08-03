from django.shortcuts import get_object_or_404
from apps.accounts.models import Student, Sponsor
from apps.payments.models import Sponsorship
from rest_framework.validators import ValidationError
from django.core.exceptions import ObjectDoesNotExist


def validate_payment(validated_data):
    student = get_object_or_404(Student, id=validated_data["student_id"])
    sponsor = get_object_or_404(Sponsor, id=validated_data["sponsor_id"])
    money = validated_data["amount"]
    try:
        instance = Sponsorship.objects.get(student_id=student.id, sponsor_id=sponsor.id)
        if money <= sponsor.balance:
            if student.balance + money <= student.contract:
                instance.amount = instance.amount + money
                sponsor.balance = sponsor.balance - money
                sponsor.sponsored = sponsor.sponsored + money
                student.balance = student.balance + money
                sponsor.save()
                student.save()
                instance.save()
                return instance
            else:
                raise ValidationError(
                    {"message": "Homiylik puli kontrakt pulidan oshib ketdi."}
                )
        else:
            raise ValidationError(
                {
                    "message": f"Homiy balansida {money} sum pul mavjud emas."
                }
            )
    except ObjectDoesNotExist:
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
                    {"message": "Homiylik summasi kontrakt summasidan oshib ketdi."}
                )
        else:
            raise ValidationError(
                {
                    "message": f"Homiy balansida {money} sum pul mavjud emas."
                }
            )
