from django.urls import path, include
from . import views 

urlpatterns = [
    path("polls/", include('polls.urls')),
    path('', views.index, name='index'),
]