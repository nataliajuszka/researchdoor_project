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
from users.models import UserProfile


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
        user = form.save(commit=True)
        user_profile = UserProfile(user=user)
        user_profile.save()
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


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



# class RegisterFormView(FormView):
#     form_class = RegisterForm
#     template_name = 'userspace/register.html'#TODO
#
#     def get(self, request):
#         if request.user.is_authenticated():
#             return redirect('/activity/')#TODO
#         return super(RegisterFormView, self).get(request)
#
#     def form_valid(self, form):
#
#         form.instance.username = slugify(
#             form.instance.first_name,
#             form.instance.last_name
#         )
#         form.instance.set_password(form.cleaned_data['password1'])
#         form.instance.save()
#
#         return render(self.request, 'userspace/register-success.html')#TODO
#
#
#
# class NewUserView(TemplateView):
#
#     template_name = 'userspace/active.html'#TODO
#
#     def get(self, request):
#         if request.session.get('new_user') is None:
#             return redirect('/activity/')#TODO
#         del request.session['new_user']
#         return super(NewUserView, self).get(request)


# class LoginFormView(FormView):
#
#     form_class = LoginForm
#     template_name = 'userspace/login.html'#TODO
#
#     def get(self, request):
#         if request.user.is_authenticated():
#             return redirect('/activity/')#TODO
#         return super(LoginFormView, self).get(request)
#
#     def get_context_data(self, **kwargs):
#         context = super(LoginFormView, self).get_context_data(**kwargs)
#         next_url = self.request.GET.get('next', None)
#         if next_url:
#             context.update({'next': next_url})
#         return context
#
#     def form_valid(self, form):
#         auth.login(self.request, form.instance)
#         next_url = self.request.POST.get('next')
#         #info = LoginData.objects.create(user=form.instance)
#         if len(next_url):
#             return redirect(next_url)
#         return redirect('/activity/')


# def logout(request):
#     auth.logout(request)
#     return redirect('user:login')
