from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from employer.models import Vacancy
from .serializers import VacancySlz, CategorySlz
from .custom_filters import filter_salary, filter_created_at

class JobViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySlz
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, filter_created_at(queryset,), filter_salary(queryset,)]
    filterset_fields = ['salary_type', "employment_form", "employment_type", "currency", 'location']




