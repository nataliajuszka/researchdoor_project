from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from news.forms import AddNewsForm
from news.models import News


class AddNewsView(CreateView):
    """
    Create news view.
    """
    model = News
    form_class = AddNewsForm
    template_name = "add_news.html"
    success_url = "/"  # TODO

    @method_decorator(login_required(login_url='/user/login/'))
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(AddNewsView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = None
        form = AddNewsForm
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form = AddNewsForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        created_news = form.save(commit=False)
        created_news.author = self.request.user
        created_news.save()
        form.save_m2m()
        created_news.organization.add(self.request.user)
        return HttpResponseRedirect(reverse("index"))    #TODO