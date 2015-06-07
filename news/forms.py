from django import forms
from news.models import News


class AddNewsForm(forms.ModelForm):
    """
    Form for adding news.
    """
    class Meta:
        model = News
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput({
                "class": "width-100",
                "placeholder": "News' title"
            }),
            "organizations": forms.CheckboxSelectMultiple(),
            "content": forms.Textarea({
                "placeholder": "News's content"
            })
        }


# class UserModelChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#          return obj.get_full_name()
