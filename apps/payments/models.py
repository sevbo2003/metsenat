from django.db import models
from apps.accounts.models import Student, Sponsor


class Sponsorship(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sponsor.full_name.split()[0]} - {self.student.full_name.split()[0]} ga {{self.amount}} sum sponsorlik qildi "
    
    class Meta:
        ordering = ["-created_at"]