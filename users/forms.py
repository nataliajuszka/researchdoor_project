__author__ = 'karolinka'
from django import forms
from users.models import UserProfile
from django import forms
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
#from django.contrib.auth.forms import AuthenticationForm
from models import UserProfile


class RegistrationForm(forms.ModelForm):
    """
    Registration form.
    """
    username = forms.CharField(
        required=True,
        help_text="Username"
    )

    email = forms.EmailField(
        required=True,
        help_text="E-mail address"
    )

    first_name = forms.CharField(
        required=True,
        help_text="First name"
    )

    last_name = forms.CharField(
        required=True,
        help_text="Last name"
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        help_text="Password"
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        help_text="Retype password"
    )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "width-100"

    def clean_username(self):
        """
        Official doc - https://docs.djangoproject.com/en/1.8/ref/forms/validation/
        Validates uniqueness of username.
        """
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).count():
            raise forms.ValidationError('User with this username address already exists.')
        return username

    def clean_email(self):
        """
        Official doc - https://docs.djangoproject.com/en/1.8/ref/forms/validation/
        Validates e-mail address.
        """
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError('User with this email address already exists.')
        return email

    def clean(self, *args, **kwargs):
        """
        Raises validation error if passwords don't match.
        :param args:
        :param kwargs:
        :return:
        """
        password1 = self.cleaned_data.get("password", None)
        password2 = self.cleaned_data.get("password2", None)

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Type the same passwords.")
        return super(RegistrationForm, self).clean()

    def save(self, commit=True):
        """
        Saves a new user in db, sets user password before commit.
        Username and email are saved in constructor of User object.
        :param commit:
        :return:
        """
        #self.fields['username'] = slugify('-'.join([self.cleaned_data["first_name"], self.cleaned_data["last_name"]]))
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', "password", "password2")


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "width-100"
            if field_name == "user_name":
                field.help_text = "User name"
            elif field_name == "password":
                field.help_text = "Password"


class UserProfileForm(forms.ModelForm):


    class Meta:
        model = UserProfile
        exclude = ('user', )






