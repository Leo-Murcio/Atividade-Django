from django.urls import path
from meus_games.views import sobre

urlpatterns = [
    path('sobre/', sobre),
]