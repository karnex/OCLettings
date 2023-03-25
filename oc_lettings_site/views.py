from django.shortcuts import render
from .models import Letting, Profile


def index(request):
    """ Home page of site."""
    return render(request, 'index.html')


def lettings_index(request):
    """ Lettings index page of site."""
    lettings_list = Letting.objects.all()
    return render(request, 'lettings_index.html', {'lettings_list': lettings_list})


def letting(request, letting_id):
    """ Letting a specific page of site."""
    letting = Letting.objects.get(id=letting_id)
    return render(request, 'letting.html', {'title': letting.title, 'address': letting.address})


def profiles_index(request):
    """List all the profiles of the site """
    profiles_list = Profile.objects.all()
    return render(request, 'profiles_index.html', {'profiles_list': profiles_list})


def profile(request, username):
    """ Display a specific profile """
    profile = Profile.objects.get(user__username=username)
    return render(request, 'profile.html', {'profile': profile})
