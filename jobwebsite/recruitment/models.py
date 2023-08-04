from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email_address = models.EmailField()
    password = models.CharField(max_length=128)
    phone_number = PhoneNumberField(unique = True, null = False, blank = False)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    QUALIFICATION_CHOICES = [
        ('Bachelors', 'Bachelors'),
        ('Masters', 'Masters'),
        ('PHD', 'PHD'),
    ]
    highest_qualifications = models.CharField(max_length=100, choices=QUALIFICATION_CHOICES)
    skills = models.TextField()

    def save(self, *args, **kwargs):
        if not self.user.password:
            self.user.set_password(self.password)
            self.user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
    
class CompanyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email_address = models.EmailField()
    password = models.CharField(max_length=128)
    phone_number = PhoneNumberField(unique = True, null = False, blank = False)
    location = models.CharField(max_length=255)
    website = models.URLField(max_length=255)
    linkedin = models.URLField(max_length=255)
    github = models.URLField(max_length=255)
    instagram = models.URLField(max_length=255)
    twitter = models.URLField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.user.password:
            self.user.set_password(self.password)
            self.user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class JobCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class JobListing(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=255, default="Variable")
    description = models.TextField()
    requirements = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ApplicationModel(models.Model):
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email_address = models.EmailField()
    phone_number = PhoneNumberField()
    why_hire = models.TextField()
    linkedin = models.URLField(max_length=255)
    github = models.URLField(max_length=255)
    instagram = models.URLField(max_length=255, blank=True)
    twitter = models.URLField(max_length=255, blank=True)
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.job_listing.title}"