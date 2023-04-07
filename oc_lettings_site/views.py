from django.shortcuts import render


def index(request):
    """ Home page of site."""
    return render(request, 'index.html')
