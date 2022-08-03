from rest_framework import viewsets
from apps.payments.serializers import SponsorshipSerializer
from apps.payments.models import Sponsorship
from apps.accounts.pagination import CustomPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class SponsorshipViewSet(viewsets.ModelViewSet):
    queryset = Sponsorship.objects.all()
    serializer_class = SponsorshipSerializer
    http_method_names = ['post', 'get', 'patch', 'delete']
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = [
        "sponsor__full_name",
        "sponsor__company",
        "student__first_name",
        "student__last_name",
    ]
    filterset_fields = ["amount"]
    pagination_class = CustomPagination

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)