from django import forms
from organizations.models import Organization


class CreateOrganizationForm(forms.ModelForm):
    """
    Form to create organization.
    """
    def clean_name(self):
        """
        Organization name must be unique and have min 4 letters.
        """
        org_name = self.cleaned_data.get("name", None)
        if org_name and Organization.objects.filter(name=org_name).count():
            raise forms.ValidationError('Group with this name exists.')

        if org_name:
            if len(org_name) < 4:
                raise forms.ValidationError("Min 4 letters!")

        return org_name

    class Meta:
        model = Organization
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput({
                "class": "width-100",
                "placeholder": "Organization's name"
            }),
            "description": forms.Textarea({
                "placeholder": "Organization's description"
            })
        }


class OrganizationsList(forms.Form):
    """
    List of organizations used when creating news.
    """
    organizations = forms.ModelChoiceField(queryset=Organization.objects.all().order_by('name'), to_field_name="name")
