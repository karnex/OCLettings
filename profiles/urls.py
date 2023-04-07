from . import views
from django.urls import path

urlpatterns = [
    path('', views.profiles_index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]
