""" apps/main/forms.py """

from datetime import date

from django import forms
from django.forms.fields import CharField, DateField
from django.forms.widgets import HiddenInput

from .models import Day


class DateChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return '{}'.format(obj.date_french())


class DayForm(forms.ModelForm):
    """ Form for Day. """
    day = DateField(
        widget=HiddenInput(),
    )
    father = CharField(
        required=False,
    )
    brother = CharField(
        required=False,
    )

    class Meta:
        model = Day
        fields = '__all__'
