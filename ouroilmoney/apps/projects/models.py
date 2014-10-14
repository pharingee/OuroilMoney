from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
from ouroilmoney.utils.models import TimeStampedPublishModel
from ouroilmoney.apps.allocations.models import AnnualBudgetAllocation
from ouroilmoney.apps.allocations.models import ConfirmAllocation


class AnnualBudgetSector(TimeStampedPublishModel):
    title = models.CharField(max_length=500, verbose_name='title of Sector')
    total_amount = models.DecimalField(
        decimal_places=3, max_digits=19,
        null=True,  blank=True)
    allocation = models.ForeignKey(
        AnnualBudgetAllocation,
        limit_choices_to={'title': 'ABFA'})

    @property
    def amount(self):
        return '${amount}'.format(amount=self.total_amount)

    def __unicode__(self):
        return '{title} {amount}'.format(
            title=self.title, amount=self.total_amount)

    class Meta:
        ordering = ('-allocation',)
        verbose_name = 'Annual Budget Report Sector'
        verbose_name_plural = 'Annual Budget Reports Sectors'


class ConfirmSector(TimeStampedPublishModel):
    total_amount = models.DecimalField(
        decimal_places=3, max_digits=19, null=True, blank=True)
    allocation = models.ForeignKey(
        ConfirmAllocation, verbose_name='choose Allocation From Other Report')
    annual_budget_sector = models.ForeignKey(
        AnnualBudgetSector,
        verbose_name="choose Sector From Annual Budget Report")

    @property
    def amount_annual_budget(self):
        return '${amount}'.format(amount=self.total_amount)

    @property
    def amount_another_report(self):
        return '${amount}'.format(amount=self.total_amount)

    def __unicode__(self):
        return '{title} {amount}'.format(
            title=self.title, amount=self.total_amount)

    class Meta:
        ordering = ('-allocation',)
        verbose_name = 'Sector from Other Report'
        verbose_name_plural = 'Other Reports Sectors'


class AnnualBudgetProject(TimeStampedPublishModel):
    amount = models.DecimalField(decimal_places=3, max_digits=19)
    name = models.CharField(max_length=500, verbose_name='name of Project')
    sector = models.ForeignKey(
        AnnualBudgetSector,
        verbose_name='choose Sector From Annual Budget Reports')

    @property
    def amount_from_annual_project(self):
        return '${amount}'.format(amount=self.amount)

    def clean(self):
        if self.amount:
            if self.amount > self.sector.amount:
                raise ValidationError(
                    "Amount for this Project cannot \
                    be more than that provided for it's sector")

    def __unicode__(self):
        return '{name} {amount}'.format(name=self.name, amount=self.amount)

    class Meta:
        ordering = ('-sector',)
        verbose_name = ('Annual Budget Report Project')
        verbose_name_plural = ('Annual Budget Reports Projects')


class ConfirmProject(TimeStampedPublishModel):
    amount = models.DecimalField(decimal_places=3, max_digits=19)
    sector = models.ForeignKey(
        ConfirmSector, verbose_name='choose Sector From Other Reports')
    project = models.ForeignKey(
        AnnualBudgetProject, verbose_name='choose Project  From Other Reports')

    @property
    def amount_from_annual_project(self):
        return '${amount}'.format(amount=self.project.amount)

    @property
    def amount_from_other_project(self):
        return '${amount}'.format(amount=self.amount)

    def clean(self):
        if self.amount:
            if self.amount > self.sector.amount:
                raise ValidationError(
                    "Amount for this Project \
                    cannot be more than that provided for it's sector")

    def __unicode__(self):
        return '{name} {amount}'.format(
            name=self.name, amount=self.total_amount)

    class Meta:
        ordering = ('-sector',)
        verbose_name = ('Project From Other Report')
        verbose_name_plural = ('Other Reports Projects')
