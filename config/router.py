from email.mime import base
from django.urls import path, include
from apps.accounts.views import UniversityViewSet, StudentViewSet, SponsorViewSet, DashboardView
from apps.payments.views import SponsorshipViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('universities', UniversityViewSet, basename='university')
router.register('students', StudentViewSet, basename='student')
router.register('sponsors', SponsorViewSet, basename='sponsor')
router.register('sponsorships', SponsorshipViewSet, basename='sponsorship')
router.register('dashboard', DashboardView, basename='dashboard')


urlpatterns = [
    path('', include(router.urls)),
]