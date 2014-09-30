from django.db import models
from ouroilmoney.apps.revenues.models import Revenues

# Create your models here.


class Allocations(models.Model):

    #choose a default revenue
    title = models.CharField(max_length= 500)
    revenue = models.ForeignKey(Revenues)
    amount  = models.DecimalField(max_length=8, decimal_places=2, max_digits=10)
    receipt = models.CharField(max_length=500, null=True, blank=True)


    @property
    def allocation_amount(self):
        return '${amount}'.format(amount=self.amount)



    def __unicode__(self):
        return '{title} {amount} {revenue}'.format(title=self.title, amount=self.amount, revenue=self.revenue)



class subAllocations(models.Model):

    title = models.CharField(max_length= 500)
    allocation = models.ForeignKey(Allocations)
    amount  = models.DecimalField(max_length=8, decimal_places=2, max_digits=10)


    @property
    def suballocation_amount(self):
        return '${amount}'.format(amount=self.amount)

    def __unicode__(self):
        return '{title} {amount} {allocation}'.format(title=self.title, amount=self.amount, revenue=self.revenue)

