from django.db import models
# from django.core.exceptions import ValidationError
# Create your models here.
from ouroilmoney.utils.models import (
    TimeStampedPublishModel,
    AmountModel,
    Region)

from ouroilmoney.apps.allocations.models import AnnualBudgetAllocation
from ouroilmoney.apps.allocations.models import ConfirmAllocation


class ProjectModel(AmountModel, TimeStampedPublishModel):

    regions = models.ManyToManyField(Region)

    town = models.CharField(
        max_length=100,
        verbose_name='town of Project',
        blank=True,
        null=True)

    # add town

    class Meta:
        abstract = True

# todo:annual budget sectors should have choices


class AnnualBudgetSector(AmountModel, TimeStampedPublishModel):
    CAPITAL_EXPENDITURE = 'CAPITAL EXPENDITURE'
    RECURRENCE_EXPENDITURE = 'RECURRENCE EXPENDITURE'

    EXPENDITURE = (
        (CAPITAL_EXPENDITURE, 'CAPITAL EXPENDITURE'),
        (RECURRENCE_EXPENDITURE, 'RECURRENCE EXPENDITURE'))

    title = models.CharField(
        max_length=500,
        verbose_name='title of Sector')

    expenditure = models.CharField(
        max_length=500,
        choices=EXPENDITURE,
        verbose_name='Capital Expenditure or Recurrence Expenditure',
        default='CAPITAL EXPENDITURE')

    allocation = models.ForeignKey(
        AnnualBudgetAllocation,
        limit_choices_to={'title': 'ABFA'})

    @property
    def amount_from_annual_budget(self):
        if self.amount is not None:
            return '{currency} {amount}'.format(
                currency=self.currency,
                amount=self.amount)

    def __unicode__(self):
        return '{title} {currency} {amount}'.format(
            title=self.title, currency=self.currency, amount=self.amount)

    class Meta:
        ordering = ('-allocation',)
        verbose_name = 'Annual Budget Sector'
        verbose_name_plural = 'Annual Budget Sectors'


class ConfirmSector(AmountModel, TimeStampedPublishModel):
    allocation = models.ForeignKey(
        ConfirmAllocation, verbose_name='choose Allocation From Other Report')
    annual_budget_sector = models.ForeignKey(
        AnnualBudgetSector,
        verbose_name="choose Sector From Annual Budget Report",
        related_name='othersectors')

    @property
    def amount_from_annual_budget(self):
        return '${amount}'.format(
            amount=self.annual_budget_sector.amount)

    @property
    def amount_another_report(self):
        return '${amount}'.format(amount=self.amount)

    def __unicode__(self):
        return '{allocation}  {allocation_amount} {amount}'.format(
            allocation=self.allocation, amount=self.amount,
            allocation_amount=self.allocation.amount)

    class Meta:
        ordering = ('-allocation',)
        verbose_name = 'Sector from Other Report'
        verbose_name_plural = 'Other Reports Sectors'


class AnnualBudgetProject(ProjectModel):
    title = models.CharField(max_length=500, verbose_name='name of Project')
    sector = models.ForeignKey(
        AnnualBudgetSector,
        verbose_name='choose Sector From Annual Budget Reports')

    @property
    def amount_from_annual_project(self):
        return '{currency} {amount}'.format(
            currency=self.currency,
            amount=self.amount)

    @property
    def sector_title(self):
        return self.sector.title

    # def clean(self):
    #     if self.amount:
    #         if self.amount > self.sector.amount:
    #             raise ValidationError(
    #                 "Amount for this Project cannot \
    #                 be more than that provided for it's sector")

    def __unicode__(self):
        return '{title} {amount}'.format(title=self.title, amount=self.amount)

    class Meta:
        ordering = ('-sector',)
        verbose_name = ('Annual Budget Project')
        verbose_name_plural = ('Annual Budget Projects')


class ConfirmProject(ProjectModel):
    ONGOIN = 'ONGOING'
    FULFILLED = 'FULFILLED'
    FAILED = 'FAILED'

    REMARKS = (
        (FAILED, 'FAILED'),
        (ONGOIN, 'ONGOING'),
        (FULFILLED, 'FULFILLED'))

    sector = models.ForeignKey(
        ConfirmSector, verbose_name='choose Sector From Other Reports')

    image = models.ImageField(
        upload_to='documents/monitoringprojects/%Y/%m/%d/',
        blank=True,
        default=None,
        null=True, verbose_name='Upload Image For Project')

    project = models.ForeignKey(
        AnnualBudgetProject,
        verbose_name='choose Project  From Other Reports',
        related_name='otherprojects')

    remarks = models.CharField(
        max_length=10,
        choices=REMARKS,
        blank=True,
        null=True)

    video = models.FileField(
        upload_to='documents/video/%Y/%m/%d/',
        verbose_name='upload Videos', null=True, blank=True)
    # may be we could restrict this field to avoid adding other documents

    def admin_image(self):
            if self.image:
                return '<img style="width:80px; \
                height:80px;"class="img-rounded" src="%s"/>'\
                % self.image.url

    admin_image.allow_tags = True

    @property
    def amount_from_annual_project(self):
        return '{currency} {amount}'.format(
            currency=self.currency,
            amount=self.project.amount)

    @property
    def amount_from_other_project(self):
        return '{currency} {amount}'.format(
            currency=self.currency,
            amount=self.amount)

    # def clean(self):
    #     if self.amount:
    #         if self.amount > self.sector.amount:
    #             raise ValidationError(
    #                 "Amount for this Project \
    #                 cannot be more than that provided for it's sector")

    def __unicode__(self):
        return '{project} {amount}  {sector}'.format(
            project=self.project, sector=self.sector, amount=self.amount)

    class Meta:
        ordering = ('-sector',)
        verbose_name = ('Monitoring Report on Project')
        verbose_name_plural = ('Monitoring Reports on Projects')
