# profiles/forms.py
from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'name', 'profile_picture',
            'guest_frequency', 'sleep_pattern', 'hobbies_interests', 'smoking_drinking', 
            'pet_friendly', 'gender', 'diet', 'personality', 'travel_pattern', 
            'state', 'major', 'degree_type', 'career_domain', 'cooking_skills', 
            'looking_for_roommate', 'location'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'guest_frequency': forms.Select(choices=[('Sometimes', 'Sometimes'), ('More often', 'More often')], attrs={'class': 'form-select mt-1 block w-full'}),
            'sleep_pattern': forms.Select(choices=[('Morning person', 'Morning person'), ('Night owl', 'Night owl')], attrs={'class': 'form-select mt-1 block w-full'}),
            'hobbies_interests': forms.CheckboxSelectMultiple(choices=[
                ('Singing', 'Singing'), ('Movies', 'Movies'), ('Cricket', 'Cricket'), ('Badminton', 'Badminton'),
                ('Reading', 'Reading'), ('Traveling', 'Traveling'), ('Cooking', 'Cooking'), ('Gaming', 'Gaming'), 
                ('Music', 'Music')
            ]),
            'smoking_drinking': forms.Select(choices=[('Occasionally', 'Occasionally'), ('Sometimes', 'Sometimes'), ('More often', 'More often')], attrs={'class': 'form-select mt-1 block w-full'}),
            'pet_friendly': forms.Select(choices=[('Yes', 'Yes'), ('No', 'No')], attrs={'class': 'form-select mt-1 block w-full'}),
            'gender': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], attrs={'class': 'form-select mt-1 block w-full'}),
            'diet': forms.Select(choices=[('Vegetarian', 'Vegetarian'), ('Non-vegetarian', 'Non-vegetarian'), ('Vegan', 'Vegan')], attrs={'class': 'form-select mt-1 block w-full'}),
            'personality': forms.Select(choices=[('Introvert', 'Introvert'), ('Extrovert', 'Extrovert'), ('Ambivert', 'Ambivert')], attrs={'class': 'form-select mt-1 block w-full'}),
            'travel_pattern': forms.Select(choices=[('Sometimes', 'Sometimes'), ('More often', 'More often')], attrs={'class': 'form-select mt-1 block w-full'}),
            'state': forms.Select(choices=[
                ('Texas', 'Texas'), ('Florida', 'Florida'), ('California', 'California'),
                ('New York', 'New York'), ('Pennsylvania', 'Pennsylvania'), ('Illinois', 'Illinois'), 
                ('Ohio', 'Ohio'), ('Georgia', 'Georgia'), ('North Carolina', 'North Carolina'), 
                ('Michigan', 'Michigan'), ('New Jersey', 'New Jersey'), ('Virginia', 'Virginia'),
                ('Washington', 'Washington'), ('Arizona', 'Arizona'), ('Massachusetts', 'Massachusetts'),
                ('Tennessee', 'Tennessee'), ('Indiana', 'Indiana'), ('Missouri', 'Missouri'),
                ('Maryland', 'Maryland'), ('Wisconsin', 'Wisconsin'), ('Colorado', 'Colorado'),
                ('Minnesota', 'Minnesota'), ('South Carolina', 'South Carolina'), ('Alabama', 'Alabama'),
                ('Louisiana', 'Louisiana'), ('Kentucky', 'Kentucky'), ('Oregon', 'Oregon'),
                ('Oklahoma', 'Oklahoma'), ('Connecticut', 'Connecticut'), ('Utah', 'Utah'),
                ('Iowa', 'Iowa'), ('Nevada', 'Nevada'), ('Arkansas', 'Arkansas'),
                ('Mississippi', 'Mississippi'), ('Kansas', 'Kansas'), ('New Mexico', 'New Mexico'),
                ('Nebraska', 'Nebraska'), ('West Virginia', 'West Virginia'), ('Idaho', 'Idaho'),
                ('Hawaii', 'Hawaii'), ('New Hampshire', 'New Hampshire'), ('Maine', 'Maine'),
                ('Montana', 'Montana'), ('Rhode Island', 'Rhode Island'), ('Delaware', 'Delaware'),
                ('South Dakota', 'South Dakota'), ('North Dakota', 'North Dakota'), ('Alaska', 'Alaska'),
                ('Vermont', 'Vermont'), ('Wyoming', 'Wyoming')
            ], attrs={'class': 'form-select mt-1 block w-full'}),
            'major': forms.Select(choices=[
                ('CS', 'Computer Science'), ('ECE', 'Electronics and Communication Engineering'), 
                ('ISOM', 'Information Systems and Operations Management'), ('Chemical', 'Chemical Engineering'),
                ('Mechanical', 'Mechanical Engineering'), ('Civil', 'Civil Engineering'),
                ('Electrical', 'Electrical Engineering'), ('Biomedical', 'Biomedical Engineering')
            ], attrs={'class': 'form-select mt-1 block w-full'}),
            'degree_type': forms.Select(choices=[('Masters', 'Masters'), ('PHD', 'PHD')], attrs={'class': 'form-select mt-1 block w-full'}),
            'career_domain': forms.Select(choices=[
                ('Founder', 'Founder'), ('Project Manager', 'Project Manager'), ('Developer', 'Developer'), 
                ('Data Analytics', 'Data Analytics'), ('Machine Learning', 'Machine Learning'), 
                ('Full-Stack', 'Full-Stack'), ('Frontend', 'Frontend'), ('Backend', 'Backend'),
                ('Mobile Development', 'Mobile Development'), ('UI/UX', 'UI/UX'), ('Network Engineering', 'Network Engineering'),
                ('Cybersecurity', 'Cybersecurity'), ('DevOps', 'DevOps'), ('Quality Assurance', 'Quality Assurance')]),
            'cooking_skills': forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '10', 'class': 'slider'}),
            'looking_for_roommate': forms.CheckboxInput(attrs={'class': 'form-checkbox mt-1 block w-full'}),
            'location': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
        }
