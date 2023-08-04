from django.contrib import admin
from .models import UserProfile, CompanyProfile, JobCategory, JobListing, ApplicationModel

class CompanyProfileAdmin(admin.ModelAdmin):
    # Customize how the CompanyProfile model is displayed in the admin
    list_display = ('user','email_address', 'password', 'phone_number', 'location', 'website', 'linkedin', 'github', 'instagram', 'twitter')

class UserProfileAdmin(admin.ModelAdmin):
    # Customize how the CompanyProfile model is displayed in the admin
    list_display = ('user','email_address', 'password', 'phone_number', 'gender', 'highest_qualifications', 'skills')

class JobCategoryAdmin(admin.ModelAdmin):
    # Customize how the CompanyProfile model is displayed in the admin
    list_display = ('name','description')

class JobListingAdmin(admin.ModelAdmin):
    # Customize how the CompanyProfile model is displayed in the admin
    list_display = ('title','company', 'category', 'location', 'salary', 'description', 'requirements', 'published_at')

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CompanyProfile, CompanyProfileAdmin)
admin.site.register(JobCategory, JobCategoryAdmin)
admin.site.register(JobListing, JobListingAdmin)
admin.site.register(ApplicationModel)