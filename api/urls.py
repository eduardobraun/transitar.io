# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'stops', views.StopViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^osm_import/$', views.osm_import),
]

