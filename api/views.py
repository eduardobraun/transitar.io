from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django.views.generic import View

from rest_framework import viewsets

from .models import Node, Stop
from .serializers import StopSerializer

from rest_framework import permissions

class StopViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    resource_name = 'stops'

