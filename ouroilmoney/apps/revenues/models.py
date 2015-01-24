from django.db import models
from django.core.exceptions import ValidationError
from ouroilmoney.apps.reports.models import AnnualBudgetReport
from ouroilmoney.utils.models import TimeStampedPublishModel
from django.db.models import Sum


class AnnualBudgetReportManager(models.Manager):

    def totalRevenue(self):
        total_revenue = self.aggregate(Sum('amount'))
        return total_revenue['amount__sum']

    def latest_revenue_date(self):
        lastest_date = self.latest('report')
        return lastest_date.report.date


# Create your models here.
class AnnualBudgetReportRevenue(TimeStampedPublishModel):
    #ABR refers to the annual budget report

    GHANACEDI = 'GHS'
    DOLLARS = '$'

    CURRENCY = ((GHANACEDI, 'GHS(GHANA CEDI)'), (DOLLARS, '$ (DOLLARS)'))

    currency = models.CharField(
        max_length='5',
        choices=CURRENCY,
        default=DOLLARS)

    report = models.ForeignKey(
        AnnualBudgetReport,
        verbose_name='choose Annual Budget Report', related_name="revenues")

    title = models.CharField(max_length=500, verbose_name='title Of Revenue')

    amount = models.DecimalField(decimal_places=2, max_digits=19,null=True,  blank=True)


    # todo:limit date based on the date from the revenue chosen
    year = models.IntegerField(max_length=4)

    # todo: year validation seems not to be working
    objects = models.Manager()
    revenue_objects = AnnualBudgetReportManager()

    def clean(self):
        if self.year:
            if self.year != self.report.date.year:
                raise ValidationError(
                    'year must equal to the year report was released')

    @property
    def revenue_amount(self):
        return '{currency} {amount}'.format(
            currency=self.currency,
            amount=self.amount)

    def __unicode__(self):
        return '{title} {year} {amount}'.format(
            title=self.title, year=self.year, amount=self.amount)

    class Meta:
        ordering = ('-year', )
        unique_together = (('title', 'year'),)
        verbose_name = 'Revenue from Annual Budget Report'
        verbose_name_plural = 'Revenues from Annual Budget Report'
