from django import forms
from organizations.models import Organization


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        exclude = ('slug', 'creator', 'users', 'publications')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control custom-wysiwyg'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'})
        }