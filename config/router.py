from django.urls import path, include
from apps.accounts.views import UniversityViewSet, StudentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('universities', UniversityViewSet, basename='university')
router.register('students', StudentViewSet, basename='student')


urlpatterns = [
    path('', include(router.urls)),
]