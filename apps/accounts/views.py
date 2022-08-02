from rest_framework import viewsets
from apps.accounts.serializers import UniversitySerializer, StudentSerializer, SponsorSerializer
from apps.accounts.models import University, Student, Sponsor
from rest_framework.permissions import IsAdminUser
from apps.accounts.pagination import CustomPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    pagination_class = CustomPagination


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["first_name", "last_name"]
    filterset_fields = ["degree", "university"]


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["full_name", "company"]
    filterset_fields = ["balance", "status", "sponsored"]