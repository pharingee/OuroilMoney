from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
from ouroilmoney.utils.models import TimeStampedPublishModel, AmountModel
from ouroilmoney.apps.allocations.models import AnnualBudgetAllocation
from ouroilmoney.apps.allocations.models import ConfirmAllocation


# todo:annual budget sectors should have choices

class AnnualBudgetSector(AmountModel,TimeStampedPublishModel):
    title = models.CharField(max_length=500, verbose_name='title of Sector')
    allocation = models.ForeignKey(
        AnnualBudgetAllocation,
        limit_choices_to={'title': 'ABFA'})

    @property
    def amount_from_annual_budget(self):
        if self.amount is not None:
            return '{currency} {amount}'.format(currency=self.currency, amount=self.amount)

    def __unicode__(self):
        return '{title} {currency} {amount}'.format(
            title=self.title, currency=self.currency, amount=self.amount)

    class Meta:
        ordering = ('-allocation',)
        verbose_name = 'Annual Budget Report Sector'
        verbose_name_plural = 'Annual Budget Reports Sectors'


class ConfirmSector(AmountModel,TimeStampedPublishModel):
    allocation = models.ForeignKey(
        ConfirmAllocation, verbose_name='choose Allocation From Other Report')
    annual_budget_sector = models.ForeignKey(
        AnnualBudgetSector,
        verbose_name="choose Sector From Annual Budget Report", related_name='othersectors')

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


class ProjectModel(AmountModel, TimeStampedPublishModel):
    GREATER = 'GREATER REGION'
    ASHANTI = 'ASHANTI REGION'
    NORTHERN = 'NORTHERN REGION'
    UPPER_EAST = 'UPPER EAST REGION'
    UPPER_WEST = 'UPPER WEST REGION'
    EASTERN = 'EASTERN REGION'
    WESTERN = 'WESTERN REGION'
    CENTRAL = 'CENTRAL REGION'
    VOLTA = 'VOLTA REGION'
    BRONG_AHAFO = 'BRONG AHAFO REGION'

    REGIONS =((GREATER, 'GREATER REGION'),
        (ASHANTI,'ASHANTI REGION'),
        (NORTHERN,'NORTHERN REGION'),
        (UPPER_WEST,'UPPER WEST REGION'),
        (UPPER_EAST,'UPPER EAST REGION'),
        (EASTERN,'EASTERN REGION'),
        (WESTERN, 'WESTERN REGION'),
        (CENTRAL, 'CENTRAL REGION'),
        (VOLTA,'VOLTA REGION'),
        (BRONG_AHAFO,'BRONG AHAFO REGION'))


    region = models.CharField(max_length=20,
        verbose_name='region of Project',
        choices=REGIONS,
        blank=True,null=True)


    class Meta:
        abstract=True

class AnnualBudgetProject(ProjectModel):

    title = models.CharField(max_length=500, verbose_name='name of Project')
    sector = models.ForeignKey(
        AnnualBudgetSector,
        verbose_name='choose Sector From Annual Budget Reports')


    @property
    def amount_from_annual_project(self):
        return '{currency} {amount}'.format(currency=self.currency,amount=self.amount)

    def clean(self):
        if self.amount:
            if self.amount > self.sector.amount:
                raise ValidationError(
                    "Amount for this Project cannot \
                    be more than that provided for it's sector")

    def __unicode__(self):
        return '{title} {amount}'.format(title=self.title, amount=self.amount)

    class Meta:
        ordering = ('-sector',)
        verbose_name = ('Annual Budget Report Project')
        verbose_name_plural = ('Annual Budget Reports Projects')


class ConfirmProject(ProjectModel):
    ONGOIN ='ONGOING'
    FULFILLED = 'FULFILLED'
    FAILED = 'FAILED'

    REMARKS = ((FAILED,'FAILED'),
        (ONGOIN,'ONGOING'),
        (FULFILLED,'FULFILLED'))

    sector = models.ForeignKey(
        ConfirmSector, verbose_name='choose Sector From Other Reports')
    project = models.ForeignKey(
        AnnualBudgetProject, verbose_name='choose Project  From Other Reports', related_name='otherprojects')
    remarks =  models.CharField(max_length=10, choices=REMARKS,blank=True,null=True)

    @property
    def amount_from_annual_project(self):
        return '{currency} {amount}'.format(currency=self.currency, amount=self.project.amount)

    @property
    def amount_from_other_project(self):
        return '{currency} {amount}'.format(currency=self.currency, amount=self.amount)

    def clean(self):
        if self.amount:
            if self.amount > self.sector.amount:
                raise ValidationError(
                    "Amount for this Project \
                    cannot be more than that provided for it's sector")

    def __unicode__(self):
        return '{project} {amount}  {sector}'.format(
            project=self.project, sector=self.sector, amount=self.amount)

    class Meta:
        ordering = ('-sector',)
        verbose_name = ('Project From Other Report')
        verbose_name_plural = ('Other Reports Projects')
