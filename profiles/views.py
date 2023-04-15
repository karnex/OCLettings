from django.shortcuts import render
from profiles.models import Profile


def index(request):
    """List all the profiles of the site """
    profiles_list = Profile.objects.all()
    return render(request, 'profiles/index.html', {'profiles_list': profiles_list})


def profile(request, username):
    """ Display a specific profile """
    profile = Profile.objects.get(user__username=username)
    return render(request, 'profiles/profile.html', {'profile': profile})
