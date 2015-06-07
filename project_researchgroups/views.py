__author__ = 'karolinka'
from django.shortcuts import render_to_response
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)
