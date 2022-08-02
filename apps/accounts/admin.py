from django.contrib import admin
from apps.accounts.models import Student, Sponsor, University


admin.site.register(Student)
admin.site.register(Sponsor)
admin.site.register(University)