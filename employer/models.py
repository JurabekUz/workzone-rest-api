import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=200)

EmploymentForm = [
    ('OF', 'In Office'),
    ('ON', 'Remote'),
    ('HY', 'Hybrid')
]

EmploymentType = [
    ('FT', 'Full-Time'),
    ('PT', 'Part-Time'),
    ('FR', 'Freelance'),
    ('CT', 'Contract'),
    ('IN', 'Internship'),
]

SalaryType = [
    ('HOUR', 'Hour'),
    ('DAY', 'Day'),
    ('MONTH', 'Month'),
    ('HM', 'Half-Month'),
    ('YEAR', 'Year')
]

Currency = [
    ('UZS', 'UZS'),
    ('RUB', 'RUB'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
]


class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(blank=True,null=True)
    staffs = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()
    telegram = models.URLField(blank=True,null=True)
    linkedin = models.URLField(blank=True,null=True)
    youtube = models.URLField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)
    facebook = models.URLField(blank=True,null=True)

    def __str__(self) -> str:
        return self.name

    def count_vacancy(self):
        return self.vacancy.count()


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
