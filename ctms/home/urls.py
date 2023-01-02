from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("matches/", matches_view, name="matches"),
    # path("teams/", TeamsPageView.as_view(), name="teams"),
    path("teams/", team_list, name = "teams"),
    path("teams/<int:teamid>", teamsview, name = "teamsview"),

    
]
