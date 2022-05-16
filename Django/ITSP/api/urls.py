import imp
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Teams, name='TeamsPage'),
    path('teams', views.apiOverview, name='apiOverview'),
    path('teams-list', views.ShowAll, name='list'),
    path('<pk>', views.ShowTeam , name='team')
]
