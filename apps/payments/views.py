from rest_framework import viewsets
from apps.payments.serializers import SponsorshipSerializer
from apps.payments.models import Sponsorship
from apps.accounts.pagination import CustomPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class SponsorshipViewSet(viewsets.ModelViewSet):
    queryset = Sponsorship.objects.all()
    serializer_class = SponsorshipSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = [
        "sponsor__full_name",
        "sponsor__company",
        "student__first_name",
        "student__last_name",
    ]
    filterset_fields = ["amount"]
    pagination_class = CustomPagination