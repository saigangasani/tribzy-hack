from django.urls import path
from .views import create_profile, find_matches, profile_success, signup, custom_login, logout_view

urlpatterns = [
    path('create_profile/', create_profile, name='create_profile'),
    path('profile_success/', profile_success, name='profile_success'),
    path('find_matches/', find_matches, name='find_matches'),
    path('signup/', signup, name='signup'),
    path('login/', custom_login, name='login'),
    path('logout/', logout_view, name='logout'),
]