from django.shortcuts import render


def index(request):
    """ Home page of site."""
    return render(request, 'index.html')


def trigger_error(request):
    division_by_zero = 1 / 0

    return division_by_zero
