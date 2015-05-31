__author__ = 'koala'
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import UserProfile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError('User with this email address already exists.')
        return email


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, label=u"email")
    password = forms.CharField(
        required = True,
        label = u"password",
        widget = forms.PasswordInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email', None)
        password = cleaned_data.get('password', None)
        user = None
        non_field_errors = []
        if email is None:
            msg = u"Brak adresu e-mail"
            self.add_error('email', msg)
        if password is None:
            msg = u"Haslo nie moze zostac puste"
            self.add_error('password', msg)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            msg = u"Nie ma uzytkowika o podanym adresie e-mail"
            non_field_errors.append(msg)
        if user is not None:
            auth_user = auth.authenticate(username=user.username, password=password)
            if auth_user is None:
                msg = u"Niepoprawne haslo"
                non_field_errors.append(msg)
            else:
                self.instance = auth_user
        if len(non_field_errors):
            self._errors[forms.forms.NON_FIELD_ERRORS] = self.error_class(non_field_errors)
            if 'email' in cleaned_data: del cleaned_data['email']
            if 'password' in cleaned_data: del cleaned_data['password']
        return cleaned_data


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(label=("first name"), max_length=64,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label=("Last name"), max_length=64,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=False, label=("About me"),
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    birth_date = forms.CharField(label=("Birth date"), required=False,
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'birth-date',
                'readonly': 'readonly',
                'placeholder': "dd/mm/yyyy",
            }))

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'description', 'birth_date')
