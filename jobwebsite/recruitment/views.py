from django.shortcuts import render, redirect
from .models import CompanyProfile, UserProfile, JobListing
from django.contrib import messages 
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate

def login_view(request):
    if request.method == 'POST':
        # Process form submission and authenticate user
        # Example:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to a protected page
            return redirect('home')
        else:
            pass
    return render(request, 'login.html')

# Create your views here.
def HomePage(request):
    company_signup_url = reverse('company_signup')
    user_signup_url = reverse('user_signup')
    return render(request, 'home.html', {'company_signup_url': company_signup_url, 'user_signup_url': user_signup_url})

def company_signup(request):
    user_signup_url = reverse('user_signup')
    if request.method == 'POST':
        company_name = request.POST['company_name']
        email_address = request.POST['email_address']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        location = request.POST['location']
        website = request.POST['website']
        linkedin = request.POST['linkedin']
        github = request.POST['github']
        instagram = request.POST['instagram']
        twitter = request.POST['twitter']

        user = User.objects.create_user(username=company_name, email=email_address)

        # Create a new CompanyProfile object
        company_profile = CompanyProfile(
            user=user,
            name=company_name,
            email_address=email_address,
            password=password,
            phone_number=phone_number,
            location=location,
            website=website,
            linkedin=linkedin,
            github=github,
            instagram=instagram,
            twitter=twitter,
        )
        company_profile.save()

        messages.success(request, 'Company profile created successfully!')
        return redirect('home')  # Redirect to the desired URL after successful signup

    return render(request, 'job_giver.html', {'user_signup_url': user_signup_url})

def user_signup(request):
    company_signup_url = reverse('company_signup')
    if request.method == 'POST':
        full_name = request.POST['name']
        email_address = request.POST['email_address']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        highest_qualifications = request.POST['highest_qualifications']
        skills = request.POST['skills']

        user = User.objects.create_user(username=full_name, email=email_address)

        # Create a new CompanyProfile object
        user_profile = UserProfile(
            user=user,
            full_name=full_name,
            email_address=email_address,
            password=password,
            phone_number=phone_number,
            gender=gender,
            highest_qualifications=highest_qualifications,
            skills=skills,
        )
        user_profile.save()

        messages.success(request, 'User profile created successfully!')
        return redirect('job_listing')  # Redirect to the desired URL after successful signup

    return render(request, 'job_seeker.html', {'company_signup_url': company_signup_url})

@login_required
def job_listing(request):
    job_listings = JobListing.objects.all()
    context = {'job_listings':job_listings}
    return render(request, 'job_listing.html', context)