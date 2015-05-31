from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, ListView
from organizations.models import Organization


class OrganizationView(DetailView):
    model = Organization
    context_object_name = 'organization'

    def get_context_data(self, **kwargs):
        context = super(OrganizationView, self).get_context_data(**kwargs)
        context['access'] = self.object.has_access(self.request.user)
        context['member'] = self.request.user in self.object.users.all()
        return context


class OrganizationCreateView(LoginRequiredMixin, CreateView):
    model = Organization
    form_class = OrganizationForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        form.save_m2m()
        obj.users.add(self.request.user)
        follow(self.request.user, obj)
        return super(OrganizationCreateView, self).form_valid(form)

class OrganizationMemberList(ListView):
    model = User
    template_name = 'organizations/member_list.html'
    paginate_by = 25
    organization = None

    def dispatch(self, *args, **kwargs):
        self.organization = get_object_or_404(Organization,
                                              slug=self.kwargs.get('slug'))
        return super(OrganizationMemberList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.organization.users.all()

    def get_context_data(self, **kwargs):
        context = super(OrganizationMemberList, self).get_context_data(**kwargs)
        context['organization'] = self.organization
        context['access'] = self.organization.has_access(self.request.user)
        return context

