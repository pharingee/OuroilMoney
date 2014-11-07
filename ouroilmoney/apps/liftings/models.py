from django.db import models
from django.core.exceptions import ValidationError
from ouroilmoney.apps.reports.models import ConfirmReport
from ouroilmoney.utils.models import TimeStampedPublishModel
import os
from django.conf import settings

# Create your models here.
class Lifting(TimeStampedPublishModel):
    report = models.ForeignKey(ConfirmReport)

    date = models.DateField()
    volume_of_lifting = models.IntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=3)
    lifting_proceed= models.DecimalField(max_digits=19, decimal_places=3)
    # todo: automatically populate lifting_proceed on save
    # todo: make sure lifting _proceed is multiplication of the barrel_price
    # and the volume
    # did not add other liftings
    # make sure u check for if choices have different years than what was chose
    # in the lifting
    lifting_receipt = models.FileField(upload_to='liftings/%Y/%m/%d/receipts', blank=True, null=True ,verbose_name='upload Lifting Receipts')

    def lifting_has_receipt(self):
        if self.lifting_receipt:
            return  True
        return False
    lifting_receipt.boolean = True

    def get_lifting_receipt(self):
       if self.lifting_receipt:
           return os.path.join(settings.MEDIA_URL,self.lifting_receipt.url)
       return None


    @property
    def price(self):
        return '${selling_price}'.format(selling_price=self.selling_price)

    def __unicode__(self):
        return '{lifting_proceed} {date} {volume}'.format(
            lifting_proceed=self.lifting_proceed,
            date=self.date, volume=self.volume_of_lifting)

    def clean(self):
        if self.date.year != self.report.date.year:
            raise ValidationError(
                'Please check date field, year of the date must be equal to the report')
        # todo:flag rather dont stop it
        # if (self.volume_of_lifting * self.selling_price) != self.lifting_proceed:
        #             raise ValidationError(
        #                 'liftings proceeds must be volume of lifting x selling price')


    class Meta:
        ordering = ('-date',)
        verbose_name = 'Lifting from Report'
        verbose_name_plural = 'Liftings from Reports'
