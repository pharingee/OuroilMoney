from django.db import models

# Create your models here.


class Lifting(models.Model):

    date=models.DateField()
    volume = models.IntegerField()
    barrel_price = models.IntegerField()
    lifting_proceed = models.IntegerField()
    # todo: automatically populate lifting_proceed on save

    @property
    def barrel_price(self):
        return '${barrel_price}'.format(barrel_price=self.barrel_price)


    def __unicode__(self):
        return '{lifting_proceed} {date} {volume}'.format(lifting_proceed=self.lifting_proceed, date=self.date, volume=self.volume )

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Lifting'
        verbose_name_plural = 'Liftings'
