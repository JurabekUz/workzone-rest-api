from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    date_birth = models.DateField()
    location = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    about_me = models.TextField()

    #Languages
    languages = models.CharField(max_length=200)

    # social network
    website = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skill')
    skill = models.CharField(max_length=50)

class Experience(models.Model):

    EmploymentType = [
        ('FT', 'Full-Time'),
        ('PT', 'Part-Time'),
        ('FR', 'Freelance'),
        ('CT', 'Contract'),
        ('IN', 'Internship'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experience')
    company = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    employment_type =  models.CharField(max_length=2, choices=EmploymentType)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    is_present = models.BooleanField(default=False)
    description = models.TextField()

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='education')
    edu_institution = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    name_degree = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    gpa = models.FloatField(null=True)




