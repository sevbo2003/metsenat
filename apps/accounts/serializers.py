from rest_framework import serializers
from apps.accounts.models import University, Student, Sponsor, TypeSponsor
from apps.accounts.validators import phone_number, full_name
from rest_framework import validators
from django.db.models import Count


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)
    university_id = serializers.IntegerField(
        allow_null=False, required=True, write_only=True
    )

    class Meta:
        model = Student
        fields = [
            "id",
            "full_name",
            "phone_number",
            "degree",
            "contract",
            "balance",
            "university",
            "university_id",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "balance"]
        extra_kwargs = {
            "full_name": {"validators": [full_name]},
            "phone_number": {"validators": [phone_number]},
        }


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = [
            "id",
            "full_name",
            "phone_number",
            "balance",
            "sponsored",
            "status",
            "sponsor_type",
            "company",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "phone_number": {
                "allow_null": False,
                "required": True,
                "validators": [phone_number],
            },
            "full_name": {
                "allow_null": False,
                "required": True,
                "validators": [full_name],
            },
            "sponsored": {"read_only": True},
        }

    def create(self, validated_data):
        sponsor_type = validated_data["sponsor_type"]
        if sponsor_type == TypeSponsor.YURIDIK:
            if validated_data["company"]:
                sponsor = Sponsor.objects.create(**validated_data)
                return sponsor
            else:
                raise validators.ValidationError("Tashlikot nomini kiriting")
        sponsor = Sponsor.objects.create(**validated_data)
        return sponsor


class DashboardSerializer:
    def __init__(self):
        self.sponsors_count = (
            Sponsor.objects.extra({"created_at": "date(created_at)"}).values("created_at").annotate(count=Count("id")).values_list("created_at", "count")
        )
        self.students_count = (
            Student.objects.extra({"created_at": "date(created_at)"}).values("created_at").annotate(count=Count("id")).values_list("created_at", "count")
        )

    @property
    def data(self):
        return self.__dict__
