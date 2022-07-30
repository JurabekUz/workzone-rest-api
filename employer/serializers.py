from rest_framework.serializers import  ModelSerializer
from .models import Vacancy, Category, Company

class CategorySlz(ModelSerializer):
    class Meta:
        model=Category
        fields = ('title',)


class VacancySlz(ModelSerializer):
    category=CategorySlz()
    class Meta:
        model=Vacancy
        fields = ('__all__')

class CompanySlz(ModelSerializer):
    class Meta:
        model=Company
        fields = ('title',)


