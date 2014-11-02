from django.db import models
from ouroilmoney.utils.models import TimeStampedPublishModel
from django.core.exceptions import ValidationError


# Create your models here.
class ReportModel(models.Model):
    # todo:change quarter choices to commaseperatedcharacterfield
    title = models.CharField(max_length=500, verbose_name='title Of Report')
    date = models.DateField(max_length=4, verbose_name='date Released')
    source_of_report = models.CharField(
        max_length=500, verbose_name='source Of Report')

    source_url = models.URLField(
        max_length=500, blank=True, null=True,
        help_text='Optional', verbose_name='url To Source')

    class Meta:
        abstract = True


class AnnualBudgetReport(TimeStampedPublishModel, ReportModel):

    # add report type
    def __unicode__(self):
        return '{title} {date} '.format(
            title=self.title, date=self.date)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Annual Budget Report'
        verbose_name_plural = 'Annual Budget Reports'


class ConfirmReport(TimeStampedPublishModel, ReportModel):

    FIRST_QUARTER = '1ST QUARTER REPORT'
    SECOND_QUARTER = '2ND QUARTER REPORT'
    THIRD_QUARTER = '3RD QUARTER REPORT'
    FOURTH_QUARTER = '4TH QUARTER REPORT'
    MONITORING_REPORT = 'MONITORING REPORT'
    OTHER = 'NONE OF THE ABOVE'

    REPORT_TYPE_CHOICES = (
        (FIRST_QUARTER, '1ST QUARTER REPORT'),
        (SECOND_QUARTER, '2ND QUARTER REPORT'),
        (THIRD_QUARTER, '3RD QUARTER REPORT'),
        (FOURTH_QUARTER, '4TH QUARTER REPORT'),
        (MONITORING_REPORT, 'MONITORING REPORT'),
        (OTHER, 'NONE OF THE ABOVE'))

    # todo:change quarter choices to commaseperatedcharacterfield
    annual_budget_report = models.ForeignKey(
        AnnualBudgetReport, related_name='otherreports')
    report_type = models.CharField(
        max_length=20, choices=REPORT_TYPE_CHOICES,
        verbose_name='type Of Report', default=FIRST_QUARTER)


    # add report type
    def __unicode__(self):
        return '{date} {title} {report_type}'.format(
            title=self.title, date=self.date, report_type=self.report_type)

    def clean(self):
        if self.date:
            if self.date.year != self.annual_budget_report.date.year:
                raise ValidationError(
                    'Year of the date released must be the same as the year for the annual budget report ')

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Other Report'
        verbose_name_plural = 'Other  Reports'
