from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import DetailView, CreateView, ListView, TemplateView
from news.models import News
from organizations.forms import CreateOrganizationForm
from organizations.models import Organization
from publications.models import Publication
from django.core.urlresolvers import reverse_lazy, reverse
from itertools import chain


class CreateOrganizationView(CreateView):
    """
    Create organization.
    """
    model = Organization
    form_class = CreateOrganizationForm
    template_name = "create_organization.html"
    success_url = "/"  # TODO

    @method_decorator(login_required(login_url='/user/login/'))
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(CreateOrganizationView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = None
        form = CreateOrganizationForm
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form = CreateOrganizationForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        new_org = form.save(commit=False)
        new_org.creator = self.request.user
        new_org.save()
        form.save_m2m()
        new_org.users.add(self.request.user)
        return HttpResponseRedirect(reverse("index"))    #TODO


class OrganizationsViewList(TemplateView):
    """
    Organizations view - when no specified organization is provided display news from all organizations.
    Login is not required.
    """
    paginate_by = 10
    context_object_name = "news"
    template_name = "organizations.html"

    def dispatch(self, *args, **kwargs):
        return super(OrganizationsViewList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        '''
        Get the list of all organizations' news.
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        #cat_list = Category.objects.all()
        news_set = News.objects.all()
        return render(request, 'organizations.html', {'news_set': news_set})
        #return self.render_to_response(self.get_context_data(photos_set=photos_set))
        #return render(request, 'base.html', {'cat_list':cat_list})


class OrganizationViewList(ListView):
    """
    Single organization view -  news and publications for organization specified in request url (pk - primary key).
    """
    model = Organization
    context_object_name = 'organization'
    template_name = 'organization.html'

    def get_queryset(self):
        """
        Combine news and publication created by the organization. Sort by date.
        :return:
        """
        self.organization = get_object_or_404(Organization, name=self.args[0])
        news_set = News.objects.filter(organization=self.organization)
        publications_set = Publication.objects.filter(mentors=self.organization)
        result_set = sorted(chain(news_set, publications_set), key=lambda instance: instance.date_created)
        return result_set

    def get_context_data(self, **kwargs):
        """
        Get organization object.
        :param kwargs:
        :return:
        """
        context = super(OrganizationViewList, self).get_context_data(**kwargs)
        context['organization'] = self.organization
        return context

