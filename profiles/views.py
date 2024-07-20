from django.shortcuts import render, redirect
from .utils import find_best_matches
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('create_profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    profile = UserProfile.objects.get(user=user)
                    return redirect('profile_success')
                except UserProfile.DoesNotExist:
                    return redirect('create_profile')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user  # Associate the profile with the authenticated user
            user_profile.save()
            return redirect('profile_success')
    else:
        form = UserProfileForm()
    return render(request, 'profiles/create_profile.html', {'form': form})

@login_required
def profile_success(request):
    return render(request, 'profiles/profile_success.html')

@login_required
def find_matches(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_profiles = UserProfile.objects.exclude(user=request.user)

    new_profile = {
        "id": user_profile.id,
        "name": user_profile.name,
        "guest_frequency": user_profile.guest_frequency,
        "sleep_pattern": user_profile.sleep_pattern,
        "hobbies_interests": user_profile.hobbies_interests.split(','),
        "smoking_drinking": user_profile.smoking_drinking,
        "pet_friendly": user_profile.pet_friendly,
        "gender": user_profile.gender,
        "diet": user_profile.diet,
        "personality": user_profile.personality,
        "travel_pattern": user_profile.travel_pattern,
        "state": user_profile.state,
        "major": user_profile.major,
        "degree_type": user_profile.degree_type,
        "career_domain": user_profile.career_domain,
        "cooking_skills": user_profile.cooking_skills
    }

    existing_profiles = [
        {
            "id": profile.id,
            "name": profile.name,
            "guest_frequency": profile.guest_frequency,
            "sleep_pattern": profile.sleep_pattern,
            "hobbies_interests": profile.hobbies_interests.split(','),
            "smoking_drinking": profile.smoking_drinking,
            "pet_friendly": profile.pet_friendly,
            "gender": profile.gender,
            "diet": profile.diet,
            "personality": profile.personality,
            "travel_pattern": profile.travel_pattern,
            "state": profile.state,
            "major": profile.major,
            "degree_type": profile.degree_type,
            "career_domain": profile.career_domain,
            "cooking_skills": profile.cooking_skills
        } for profile in user_profiles
    ]

    matches = find_best_matches(new_profile, existing_profiles)

    return render(request, 'profiles/matches.html', {'matches': matches})

def logout_view(request):
    logout(request)
    return redirect('login')