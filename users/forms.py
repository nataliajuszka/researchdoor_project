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

# class UserLoginForm(forms.Form):
#     """
#     Login form, thanks to which we can log in by e-mail. By default django uses username.
#     """
#     email = forms.EmailField(required=True)
#     password = forms.CharField(
#         required=True,
#         widget=forms.PasswordInput()
#     )
#
#     def clean(self):
#         """
#         Get user with specified e-mail, check their username and authenticate.
#         Check for errors.
#         :return:
#         """
#         cleaned_data = super(UserLoginForm, self).clean()
#         email = cleaned_data.get('email', None)
#         password = cleaned_data.get('password', None)
#         user = None
#         non_field_errors = []
#         if email is None:
#             self.add_error('email', 'No e-mail specified')
#         if password is None:
#             self.add_error('password', 'No password specified')
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             non_field_errors.append('No user found with specified e-mail address')
#         if user is not None:
#             auth_user = auth.authenticate(username=user.username, password=password)
#             if auth_user is None:
#                 non_field_errors.append('Wrong password')
#             else:
#                 self.instance = auth_user
#         if len(non_field_errors):
#             self._errors[forms.forms.NON_FIELD_ERRORS] = self.error_class(non_field_errors)
#             if 'email' in cleaned_data:
#                 del cleaned_data['email']
#             if 'password' in cleaned_data:
#                 del cleaned_data['password']
#         return cleaned_data
# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     password1 = forms.CharField(required=True, widget=forms.PasswordInput())
#     password2 = forms.CharField(required=True, widget=forms.PasswordInput())
#
#     class Meta:
#         model = User
#         fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if email and User.objects.filter(email=email).count():
#             raise forms.ValidationError('User with this email address already exists.')
#         return email


# class UserLoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs["class"] = "width-100"
#             if field_name == "user_name":
#                 field.help_text = "User name"
#             elif field_name == "password":
#                 field.help_text = "Password"


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
