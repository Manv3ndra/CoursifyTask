# Generated by Django 4.2.2 on 2023-08-03 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('location', models.CharField(max_length=255)),
                ('website', models.URLField(max_length=255)),
                ('linkedin', models.URLField(max_length=255)),
                ('github', models.URLField(max_length=255)),
                ('instagram', models.URLField(max_length=255)),
                ('twitter', models.URLField(max_length=255)),
                ('logo', models.ImageField(upload_to='company_logos/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('highest_qualifications', models.CharField(choices=[('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('PHD', 'PHD')], max_length=100)),
                ('skills', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.jobcategory')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.companyprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('why_hire', models.TextField()),
                ('linkedin', models.URLField(max_length=255)),
                ('github', models.URLField(max_length=255)),
                ('instagram', models.URLField(blank=True, max_length=255)),
                ('twitter', models.URLField(blank=True, max_length=255)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('job_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.joblisting')),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.userprofile')),
            ],
        ),
    ]
