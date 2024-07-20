from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    guest_frequency = models.CharField(max_length=50, choices=[('Sometimes', 'Sometimes'), ('More often', 'More often')], null=True, blank=True)
    sleep_pattern = models.CharField(max_length=50, choices=[('Morning person', 'Morning person'), ('Night owl', 'Night owl')], null=True, blank=True)
    hobbies_interests = models.CharField(max_length=255, null=True, blank=True)
    smoking_drinking = models.CharField(max_length=50, choices=[('Occasionally', 'Occasionally'), ('Sometimes', 'Sometimes'), ('More often', 'More often')], null=True, blank=True)
    pet_friendly = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], null=True, blank=True)
    gender = models.CharField(max_length=50, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True, blank=True)
    diet = models.CharField(max_length=50, choices=[('Vegetarian', 'Vegetarian'), ('Non-vegetarian', 'Non-vegetarian'), ('Vegan', 'Vegan')], null=True, blank=True)
    personality = models.CharField(max_length=50, choices=[('Introvert', 'Introvert'), ('Extrovert', 'Extrovert'), ('Ambivert', 'Ambivert')], null=True, blank=True)
    travel_pattern = models.CharField(max_length=50, choices=[('Sometimes', 'Sometimes'), ('More often', 'More often')], null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    major = models.CharField(max_length=50, null=True, blank=True)
    degree_type = models.CharField(max_length=50, choices=[('Masters', 'Masters'), ('PHD', 'PHD')], null=True, blank=True)
    career_domain = models.CharField(max_length=50, null=True, blank=True)
    cooking_skills = models.IntegerField(null=True, blank=True)
    looking_for_roommate = models.BooleanField(default=True)
    location = models.CharField(max_length=255, null=True, blank=True)
