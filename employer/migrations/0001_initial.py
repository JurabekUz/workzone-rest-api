# Generated by Django 4.0.2 on 2022-07-30 08:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('website', models.URLField(blank=True, null=True)),
                ('staffs', models.PositiveSmallIntegerField()),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField()),
                ('telegram', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=150, null=True)),
                ('employment_form', models.CharField(choices=[('OF', 'In Office'), ('ON', 'Remote'), ('HY', 'Hybrid')], max_length=2)),
                ('employment_type', models.CharField(choices=[('FT', 'Full-Time'), ('PT', 'Part-Time'), ('FR', 'Freelance'), ('CT', 'Contract'), ('IN', 'Internship')], max_length=2)),
                ('salary1', models.IntegerField(blank=True, null=True)),
                ('salary2', models.IntegerField(blank=True, null=True)),
                ('salary_type', models.CharField(choices=[('HOUR', 'Hour'), ('DAY', 'Day'), ('MONTH', 'Month'), ('HM', 'Half-Month'), ('YEAR', 'Year')], max_length=5)),
                ('currency', models.CharField(choices=[('UZS', 'UZS'), ('RUB', 'RUB'), ('USD', 'USD'), ('EUR', 'EUR')], max_length=3)),
                ('experience', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('languages', models.CharField(max_length=200)),
                ('edu_level', models.CharField(default='-', max_length=150)),
                ('description', models.TextField()),
                ('contact', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateField(default=datetime.date(2022, 7, 30))),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacancy', to='employer.category')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacancy', to='employer.company')),
            ],
        ),
        migrations.CreateModel(
            name='Applied',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=512)),
                ('applied_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply', to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply', to='employer.vacancy')),
            ],
        ),
    ]
