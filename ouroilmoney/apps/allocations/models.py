from django.db import models
from django.core.exceptions import ValidationError

from ouroilmoney.apps.reports.models import AnnualBudgetReport
from ouroilmoney.apps.reports.models import ConfirmReport
from ouroilmoney.utils.models import TimeStampedPublishModel

# Create your models here.


class AnnualBudgetAllocation(TimeStampedPublishModel):
    #choose a default revenu
    report = models.ForeignKey(AnnualBudgetReport)
    title = models.CharField(
        max_length=500, default='ABFA',
        verbose_name='title Of Allocation',
        help_text='for ABFA allocations just use default')

    amount = models.CommaSeparatedIntegerField(
        max_length=40, verbose_name='amount Of Money')

    @property
    def allocated_amount(self):
        return '${amount}'.format(amount=self.amount)

    def __unicode__(self):
        return '{title} {report}'.format(
            title=self.title, report=self.report)

    class Meta:
        ordering = ('report',)
        unique_together = ('title', 'report')
        verbose_name = 'Annual Budget Allocation'
        verbose_name_plural = 'Annual Budget Allocations'


class ConfirmAllocation(TimeStampedPublishModel):

    annual_budget_allocation = models.ForeignKey(AnnualBudgetAllocation,related_name='otherallocations')
    report = models.ForeignKey(ConfirmReport, verbose_name='Other Report in the same year')
    amount = models.CommaSeparatedIntegerField(
        max_length=40, verbose_name='amount Of Money')

    @property
    def allocated_amount(self):
        return '${amount}'.format(amount=self.amount)

    @property
    def annual_budget_allocation_amount(self):
        return '${amount}'.format(amount=self. annual_budget_allocation.amount)

    def clean(self):
        #todo:validate this when everything is empty there is an error
        if self.report:
            if self.report.date.year < self.annual_budget_allocation.report.date.year:
                raise ValidationError(
                    'Report Year cannot have a report whose year is less than the year for  annual budget allocation. They must have the same year')

            elif self.report.date.year > self.annual_budget_allocation.report.date.year:
                raise ValidationError(
                    'Report field cannot have a report whose year is greater than the year for  annual budget allocation. They must have the same year')

    def __unicode__(self):
        return ' {amount} {report}'.format(
            amount=self.amount, report=self.report)

    class Meta:
        # todo: order by report's date
        verbose_name = 'Allocation from Other Report'
        verbose_name_plural = 'Allocations from other Reports'



# you can only have one sector from abfa
