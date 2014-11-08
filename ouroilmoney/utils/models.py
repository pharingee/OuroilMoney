from django.db import models

# Create your models here.

# Create your models here.
class AmountModel(models.Model):
    GHANACEDI = 'GHS'
    DOLLARS = '$'

    CURRENCY = ((GHANACEDI,'GHS(GHANA CEDI)'), (DOLLARS,'$ (DOLLARS)'))

    amount = models.DecimalField(decimal_places=2, max_digits=19,null=True,  blank=True)

    currency= models.CharField(max_length='5', choices=CURRENCY, default=DOLLARS)

    class Meta:
        abstract=True


class TimeStampedPublishModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name='publish')
    summary = models.TextField(
        null=True, blank=True,
        help_text='Please copy and past summary of Report here.\n Optional')

    class Meta:
        abstract = True
