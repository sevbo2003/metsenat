from rest_framework import viewsets
from apps.accounts.serializers import UniversitySerializer
from apps.accounts.models import University, Student, Sponsor
from rest_framework.permissions import IsAdminUser
from apps.accounts.pagination import CustomPagination


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomPagination