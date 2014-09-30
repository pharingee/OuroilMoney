from django.db import models

# Create your models here.


class Allocation(models.Model):
    #choose a default revenue
    title = models.CharField(
        max_length=500, default='ABFA',
        help_text="For annual budget Funding Amount, please choose default(ABFA)",
        verbose_name='title Of Allocation')

    amount = models.CommaSeparatedIntegerField(
        max_length=40, verbose_name='amount Of Money')

    year = models.IntegerField(max_length=4)



    @property
    def allocation_amount(self):
        return '${amount}'.format(amount=self.amount)

    def __unicode__(self):
        return '{title} {amount} {revenue}'.format(
            title=self.title, amount=self.amount, revenue=self.revenue)



# you can only have one sector from abfa
