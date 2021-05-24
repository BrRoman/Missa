""" apps/main/forms.py """

from django import forms

from .models import Day


class DayForm(forms.ModelForm):
    """ Form for Day. """
    destination = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'w-100',
            },
        ),
    )

    class Meta:
        model = Day
        fields = '__all__'
