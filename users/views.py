from django.template import RequestContext


__author__ = 'karolinka'
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from users.models import UserProfile
from users.forms import UserProfileForm
from django.contrib import auth
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import FormView, TemplateView, CreateView
from users.forms import RegistrationForm, UserLoginForm
from django.contrib.auth import login, authenticate, logout
from users.models import UserProfile,File






def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def update_profile(request):

    userProfile = UserProfile.objects.get(user=request.user)
    form = UserProfileForm(initial={"description":userProfile.description, "birth_date":userProfile.birth_date, "avatar":userProfile.avatar, "thumbnail":userProfile.thumbnail, "image":userProfile.image})
    return render_to_response('update_profile.html', {'form':form}, RequestContext(request))

def profile(request):

    userProfile = UserProfile.objects.get(user=request.user)
    return render_to_response('profile.html', {'userProfile':userProfile}, RequestContext(request))



@login_required
def send_update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            userProfile = UserProfile.objects.get(user=request.user)
            description = form.cleaned_data['description']
            userProfile.description = description
            birth_date = form.cleaned_data['birth_date']
            userProfile.birth_date = birth_date
            avatar = form.cleaned_data['avatar']
            userProfile.avatar = avatar
            thumbnail = form.cleaned_data['thumbnail']
            userProfile.thumbnail = thumbnail
            image = form.cleaned_data['image']
            userProfile.image = image
          #  avatar = form.cleaned_data['avatar']

           # imagefile = File.objects.get(file=avatar)
            #UserProfile.avatar = imagefile
            userProfile.save()
            return redirect('/user/profile')

        return redirect('http://127.0.0.1:8000/')

    else:
        form = UserProfileForm()

    return redirect('/user/profile')

class RegistrationView(CreateView):
    """
    Registration view.
    """
    model = User
    form_class = RegistrationForm
    template_name = "user_registration.html"
    success_url = "/"

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(RegistrationView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("index"))
        self.object = None
        form = RegistrationForm
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        """
        Validates if the posted form is correct.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.object = None
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        Form is validated correctly - creates a new user and their profile. User is authenticated and redirected
        to the main page.
        :param form:
        :return:
        """
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user=form.save(commit=True)
       # print user
        UserProfile.objects.get_or_create(user=user)
       # user_profile1 = UserProfile(user=user)
        #user_profile1.create(user.id)
        #user_profile1=UserProfile(description='lakakka')
       # user_profile1.save()
        authenticated = authenticate(username=username, password=password)
        login(self.request, authenticated)
        return HttpResponseRedirect(reverse("index"))

    def form_invalid(self, form):
        """
        Form is invalid.
        :param form:
        :return:
        """
        return self.render_to_response(self.get_context_data(
            form=form,
        ))


class UserLoginView(FormView):
    """
    Login view.
    """
    form_class = UserLoginForm
    template_name = "user_login.html"

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(UserLoginView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid user is authenticated and redirected to the main page.
        :param form:
        :return:
        """
        login(self.request, form.get_user())
        #username = form.cleaned_data["username"]
        return HttpResponseRedirect(reverse("index"))

    # def get_success_url(self, username):    # ???
    #     next_url = self.request.GET.get("next", None)
    #     if not next_url:
    #         next_url = reverse_lazy("account_info", kwargs={"username": username})
    #     return next_url

    def get(self, request, *args, **kwargs):
        """
        If the user is already logged in redirects to the main page, else renders form.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("index"))
        return super(UserLoginView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Validates if the posted form is correct.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)






