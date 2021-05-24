""" apps/main/views.py """

from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import DayForm
from .models import Day


def home(request):
    """ Home view of missa. """
    days = Day.objects.filter(day__year=date.today().year).order_by('day')
    return render(
        request,
        'main/home.html',
        {
            'days': days,
        }
    )


def update(request, **kwargs):
    """ Update a day. """
    day = Day.objects.get(pk=kwargs['pk'])

    if request.method == 'POST':
        form = DayForm(request.POST, instance=day)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:home'))

    else:
        form = DayForm(instance=day)

    return render(
        request,
        'main/form.html',
        {
            'form': form,
            'day': day,
        }
    )
