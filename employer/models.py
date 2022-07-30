import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model

from model_choices import *

User = get_user_model()
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    logo = models.ImageField(null=True)
    website = models.URLField(blank=True,null=True)
    staffs_count = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()
    #social network accounts
    telegram = models.URLField(blank=True,null=True)
    linkedin = models.URLField(blank=True,null=True)
    youtube = models.URLField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)
    facebook = models.URLField(blank=True,null=True)

    def __str__(self) -> str:
        return self.name

    def count_vacancy(self):
        return self.vacancy.count()

    def clean(self):
        if not self.user.is_employer:
            raise ValidationError(
                {'Error': "User is Empoler True bo'lishi kerak"})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Vacancy(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancy', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='vacancy', blank=True, null=True)
    title = models.CharField(max_length=150)
    deadline = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=150, blank=True, null=True)
    employment_form =  models.CharField(max_length=2, choices=EmploymentForm)
    employment_type =  models.CharField(max_length=2, choices=EmploymentType)
    salary1 = models.IntegerField(blank=True, null=True)
    salary2 = models.IntegerField(blank=True, null=True)
    salary_type = models.CharField(max_length=5, choices=SalaryType)
    currency = models.CharField(max_length=3, choices=Currency)
    experience = models.PositiveSmallIntegerField(blank=True, null=True)
    languages = models.CharField(max_length=200)
    edu_level = models.CharField(max_length=150, default="-")
    description = models.TextField()
    contact = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateField(default=datetime.date.today())

    def __str__(self) -> str:
        return self.title

    def update_deadline(self, date):
        self.deadline = date
        self.save()

    def update_exp(self, new):
        self.experience = new
        self.save()

    def update_salary1(self, salary):
        self.salary1 = salary
        self.save()
    
    def update_salary2(self, salary):
        self.salary2 = salary
        self.save()

    def applies_count(self):
        return self.apply.count()

class Applied(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='apply')
    user = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='apply')
    message = models.CharField(max_length=512)
    applied_date = models.DateField(auto_now_add=True)
    # apply status
    status = models.CharField(max_length=2, choices=APPLY_STATUS, default='UR')
