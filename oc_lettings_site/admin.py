from django.contrib import admin

from .models import Profile
from lettings.models import Letting, Address


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
