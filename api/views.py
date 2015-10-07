from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django.views.generic import View

from rest_framework import viewsets

from .models import Node, Stop
from .serializers import StopSerializer

from django.contrib.gis.geos import Point

from rest_framework import permissions

class StopViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    resource_name = 'stops'

def osm_import(request):
    import requests
    interpreter = 'http://overpass-api.de/api/interpreter?data='
    query = '[out:json];\
             area[name="{}"][admin_level="2"]->.country;\
             area[name="{}"][admin_level="4"]->.state;\
             area[name="{}"][admin_level="8"]->.city;\
             (node(area.city)(area.state)(area.country)[highway="bus_stop"];\
             );\
             out meta;'
    html = ""
    r = requests.get(interpreter+query.format("Brasil","Rio Grande do Sul", "Santa Maria"))
    if (r.status_code == 200):
        i=0
        for e in r.json()['elements']:
            if (Stop.objects.filter(osm_id=e['uid']).count() == 0):
                ns = Stop(name="SM-{}".format(i), pos=Point(e['lat'],e['lon']),
                          osm_id=e['uid'], osm_data=e.__str__())
                ns.save()
            i+=1
        html = "<html><body>ok.</body></html>"
    else:
        html = "<html><body>fail.</body></html>"
    return HttpResponse(html)
