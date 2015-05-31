from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from users.forms import RegisterForm, LoginForm
from django.template.defaultfilters import slugify
from users.models import LoginData


class RegisterFormView(FormView):
    form_class = RegisterForm
    template_name = 'userspace/register.html'#TODO

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('/activity/')#TODO
        return super(RegisterFormView, self).get(request)

    def form_valid(self, form):

        form.instance.username = slugify(
            form.instance.first_name,
            form.instance.last_name
        )
        form.instance.set_password(form.cleaned_data['password1'])
        form.instance.save()

        return render(self.request, 'userspace/register-success.html')#TODO



class NewUserView(TemplateView):

    template_name = 'userspace/active.html'#TODO

    def get(self, request):
        if request.session.get('new_user') is None:
            return redirect('/activity/')#TODO
        del request.session['new_user']
        return super(NewUserView, self).get(request)


class LoginFormView(FormView):

    form_class = LoginForm
    template_name = 'userspace/login.html'#TODO

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('/activity/')#TODO
        return super(LoginFormView, self).get(request)

    def get_context_data(self, **kwargs):
        context = super(LoginFormView, self).get_context_data(**kwargs)
        next_url = self.request.GET.get('next', None)
        if next_url:
            context.update({'next': next_url})
        return context

    def form_valid(self, form):
        auth.login(self.request, form.instance)
        next_url = self.request.POST.get('next')
        #info = LoginData.objects.create(user=form.instance)
        if len(next_url):
            return redirect(next_url)
        return redirect('/activity/')


def logout(request):
    auth.logout(request)
    return redirect('user:login')
