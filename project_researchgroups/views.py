from django.shortcuts import render_to_response
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


def custom_500(request):
    return render_to_response('500.html')


def custom_404(request):
    return render_to_response('404.html')
