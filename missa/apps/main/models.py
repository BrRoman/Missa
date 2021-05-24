""" apps/main/models.py """

from django.db import models


class Day(models.Model):
    """ Day model. """
    day = models.DateField(
        db_column='Date_messe',
    )
    father = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        db_column='Pere',
    )
    brother = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        db_column='Frere',
    )

    class Meta:
        managed = False
        db_table = 'Messe'

    def __str__(self):
        return '{}: {} servi par {}'.format(str(self.day), self.father if self.father else '-', self.brother if self.brother else '-')

    def date_french(self):
        """ Converts a date into french format. """
        weekdays = ['Lundi', 'Mardi', 'Mercredi',
                    'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        months = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin',
                  'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
        weekday = weekdays[self.day.weekday()]
        day = self.day.day if self.day.day != 1 else '1er'
        month = months[self.day.month - 1]
        year = self.day.year
        return '{} {} {} {}'.format(weekday, day, month, year)
