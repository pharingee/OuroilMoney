from django.db import models
from django.core.exceptions import ValidationError
from ouroilmoney.apps.reports.models import AnnualBudgetReport
from ouroilmoney.utils.models import TimeStampedPublishModel


# Create your models here.
class AnnualBudgetReportRevenue(TimeStampedPublishModel):
    #ABR refers to the annual budget report
    report = models.ForeignKey(
        AnnualBudgetReport,
        verbose_name='choose Annual Budget Report', related_name="revenues")

    title = models.CharField(max_length=500, verbose_name='title Of Revenue')
    amount = models.CommaSeparatedIntegerField(
        max_length=40, verbose_name='amount Of Money  ')
    # todo:limit date based on the date from the revenue chosen
    year = models.IntegerField(max_length=4)
    # todo: year validation seems not to be working

    def clean(self):
        if self.year:
            if self.year != self.report.date.year:
                raise ValidationError(
                    'year must equal to the year report was released')

    @property
    def revenue_amount(self):
        return '${amount}'.format(amount=self.amount)

    def __unicode__(self):
        return '{title} {year} {amount}'.format(
            title=self.title, year=self.year, amount=self.amount)

    class Meta:
        ordering = ('-year', )
        verbose_name = 'Revenue from Annual Budget Report'
        verbose_name_plural = 'Revenues from Annual Budget Report'
