from email.policy import default
from django.db import models


class University(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class DegreeType(models.TextChoices):
    BACHELOR = "BACHELOR", "Bakalavr"
    MAGISTER = "MAGISTER", "Magister"


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    degree = models.CharField(max_length=10, choices=DegreeType.choices)
    contract = models.PositiveIntegerField()
    balance = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.full_name


class StatusSponsor(models.TextChoices):
    MODERATION = "MODERATION", "Moderatsiya"
    NEW = "NEW", "Yangi"
    APPROVED = "APPROVED", "Tasdiqlangan"
    CANCELED = "CANCELED", "Bekor qilingan"


class TypeSponsor(models.TextChoices):
    JISMONIY = "JISMONIY", "Jismoniy shaxs"
    YURIDIK = "YURIDIK", "Yuridik shaxs"


class Sponsor(models.Model):
    full_name = models.CharField(max_length=100)
    sponsor_type = models.CharField(max_length=15, choices=TypeSponsor.choices)
    balance = models.PositiveIntegerField()
    sponsored = models.PositiveIntegerField(default=0)
    phone_number = models.IntegerField()
    company = models.CharField(max_length=256, null=True)
    status = models.CharField(max_length=32, choices=StatusSponsor.choices, default=StatusSponsor.MODERATION)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.amount}"
