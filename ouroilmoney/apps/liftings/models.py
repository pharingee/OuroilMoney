from django.db import models
from ouroilmoney.apps.revenues.models import Revenue


# Create your models here.


class Lifting(models.Model):
    revenue = models.ForeignKey(Revenue)
    date = models.DateField()
    volume = models.IntegerField()
    barrel_price = models.IntegerField()
    lifting_proceed = models.IntegerField()

    # todo: automatically populate lifting_proceed on save
    # todo: make sure lifting _proceed is multiplication of the barrel_price
    # and the volume
    # the revenue tied to a lifting can be
    # anything else other than the annual budget
    # did not add other liftings

    @property
    def price(self):
        return '${barrel_price}'.format(barrel_price=self.barrel_price)

    def __unicode__(self):
        return '{lifting_proceed} {date} {volume}'.format(
            lifting_proceed=self.lifting_proceed,
            date=self.date, volume=self.volume)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Lifting'
        verbose_name_plural = 'Liftings'
