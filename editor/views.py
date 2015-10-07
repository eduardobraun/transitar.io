# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView

from django.contrib.gis.geos import Point
from api.models import *

class EditorView(TemplateView):
    template_name = "editor/home.html"

    def get_context_data(self, **kwargs):
        context = super(EditorView, self).get_context_data(**kwargs)
        query_res = Stop.objects.all()
        context["stops"] = query_res
        return context

