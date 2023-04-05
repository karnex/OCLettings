from django.shortcuts import render
from .models import Profile


def index(request):
    """ Home page of site."""
    return render(request, 'index.html')


def profiles_index(request):
    """List all the profiles of the site """
    profiles_list = Profile.objects.all()
    return render(request, 'profiles_index.html', {'profiles_list': profiles_list})


def profile(request, username):
    """ Display a specific profile """
    profile = Profile.objects.get(user__username=username)
    return render(request, 'profile.html', {'profile': profile})
