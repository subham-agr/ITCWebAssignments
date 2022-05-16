import imp
from os import rename
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TeamSerializer
from . models import Team

# Create your views here.
def Teams(request):
    return render(request, 'index.html')

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/teams-list',
        'Detail View': '/team-detail/<id>',
    }

    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ShowTeam(request, pk):
    team = Team.objects.get(id=pk)
    serializer = TeamSerializer(team, many=False)
    return Response(serializer.data)