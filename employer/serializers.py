from rest_framework.serializers import  ModelSerializer
from .models import Vacancy, Category, Company, Applied

class CategorySlz(ModelSerializer):
    class Meta:
        model=Category
        fields = ('title', 'slug')

class VacancySlz(ModelSerializer):
    category=CategorySlz()
    class Meta:
        model=Vacancy
        fields = ('__all__')

class CompanySlz(ModelSerializer):
    class Meta:
        model=Company
        fields = ('__all__')

class Title_VacancySlz(ModelSerializer):
    category=CategorySlz()
    class Meta:
        model=Vacancy
        fields = ('title',)

#faqat empoler koradi
class AppliedSlz(ModelSerializer):
    # vacancy = VacancySlz('title')
    vacancy = Title_VacancySlz()
    class Meta:
        model=Applied
        fields = ('__all__')

class Name_CompanySlz(ModelSerializer):
    class Meta:
        model=Company
        fields = ('name', 'logo')
