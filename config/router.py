from django.urls import path, include
from apps.accounts.views import UniversityViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('universities', UniversityViewSet, basename='university')


urlpatterns = [
    path('', include(router.urls)),
]