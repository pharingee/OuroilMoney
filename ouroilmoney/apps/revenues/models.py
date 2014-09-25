from django.db import models
from reports.models import Report


# Create your models here.


class Revenues(models.Model):

    revenue = models.ForeignKey(Report)
    title = models.CharField(max_length=500)
    amount = models.DecimalField(max_length=8, decimal_places=2)
    year = models.IntegerField(max_length=4)


    @property
    def amount(self):
        return '${amount}'.format(amount=self.amount)


    def __unicode__(self):
        return '{title} {year} {amount}'.format(title=self.title, year=self.year)

