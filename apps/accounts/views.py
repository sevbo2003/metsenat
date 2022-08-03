from rest_framework import viewsets
from apps.accounts.serializers import UniversitySerializer, StudentSerializer, SponsorSerializer, DashboardSerializer
from apps.payments.serializers import SponsorshipSerializer
from apps.accounts.models import University, Student, Sponsor
from apps.payments.models import Sponsorship
from apps.accounts.pagination import CustomPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum


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

    @action(detail=True, methods=["get"])
    def sponsors(self, request, pk=None):
        student = self.get_object()
        queryset = student.sponsorship_set.all()
        serializer = SponsorshipSerializer(queryset, many=True)
        return Response(serializer.data)


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["full_name", "company"]
    filterset_fields = ["balance", "status", "sponsored"]

    @action(detail=True, methods=['get'])
    def sponsored(self, request, pk=None):
        sponsor = self.get_object()
        queryset = sponsor.sponsorship_set.all()
        serializer = SponsorshipSerializer(queryset, many=True)
        return Response(serializer.data)



class DashboardView(viewsets.ViewSet):
    def list(self, request):
        return Response({
            "payed": Sponsorship.objects.aggregate(Sum('amount'))['amount__sum'],
            "asked": Student.objects.aggregate(Sum('contract'))['contract__sum'],
            "should_payed": Student.objects.aggregate(Sum('contract'))['contract__sum'] - Sponsorship.objects.aggregate(Sum('amount'))['amount__sum'],
        })
    
    @action(detail=False, methods=['get'])
    def graph(self, request):
        return Response(DashboardSerializer().data)