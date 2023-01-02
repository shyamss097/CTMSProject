from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import *
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib import messages



class HomePageView(ListView):
    model = Player
    template_name = "home.html"

# class TeamsPageView(ListView):
#     model = Team
#     template_name = "teams.html"

class MatchesPageView(ListView):
    model = Matches
    template_name = "matches.html"


def team_list(request):
    # cursor = connection.cursor
    # cursor.execute("SELECT * FROM TEAM")
    data = Team.objects.raw("SELECT * FROM team")
    print(data)
    print(connection.queries)
    return render(request, 'teams.html', {'teamslist': data})

def teamsview(request, teamid):
    if(Team.objects.filter(teamid=teamid)):
        players = Player.objects.filter(teamid=teamid)
        context = {'players': players}
        return render(request, "team_details.html", context)
    else:
        messages.warning(request, "No such team found!")
        return redirect('teams')

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def matches_view(request):
    matches = Matches.objects.raw("SELECT * from matches")
    
    
    return render(request, "matches.html", {'matches': matches})

def findTeamName(id):
    teamname = Team.objects.raw("Select teamname from team where teamid=id")
    return(teamname)

def current_matches(request):
    matches = Matches.objects.raw("Select * from matches wherer date=")