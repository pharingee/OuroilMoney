from django.db import models
from ouroilmoney.apps.reports.models import Reports


# Create your models here.




class Revenues(models.Model):

    report = models.ForeignKey(Reports)
    title = models.CharField(max_length=500)
    amount = models.DecimalField(max_length=8, decimal_places=2, max_digits=10)
    year = models.IntegerField(max_length=4)


    @property
    def revenue_amount(self):
        return '${amount}'.format(amount=self.amount)


    def __unicode__(self):
        return '{title} {year} {amount}'.format(title=self.title, year=self.year)

