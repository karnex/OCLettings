from django.shortcuts import render
from .models import Letting


def lettings_index(request):
    """ Lettings index page of site."""
    lettings_list = Letting.objects.all()
    return render(request, 'lettings/lettings_index.html', {'lettings_list': lettings_list})


def letting(request, letting_id):
    """ Letting a specific page of site."""
    letting = Letting.objects.get(id=letting_id)
    return render(request, 'lettings/letting.html', {'title': letting.title, 'address': letting.address})