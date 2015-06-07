from calen.models import Entry
from django import forms

__author__ = 'koala'


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['title', 'date', 'start_time', 'end_time', 'is_weekly']
