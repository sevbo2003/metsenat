from email.mime import base
from django.urls import path, include
from apps.accounts.views import UniversityViewSet, StudentViewSet, SponsorViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('universities', UniversityViewSet, basename='university')
router.register('students', StudentViewSet, basename='student')
router.register('sponsors', SponsorViewSet, basename='sponsor')


urlpatterns = [
    path('', include(router.urls)),
]