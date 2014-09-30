from django.db import models

# Create your models here.


class Report(models.Model):
    FIRST_REPORT = 'ABR'
    FIRST_QUARTER = '1Q'
    SECOND_QUARTER = '2Q'
    THIRD_QUARTER = '3Q'
    FOURTH_QUARTER = '4Q'
    OTHER = 'NFTA'

    REPORT_TYPE_CHOICES = (
        (FIRST_REPORT, 'ANNUAL BUDGET REPORT'),
        (FIRST_QUARTER, '1ST QUARTER REPORT'),
        (SECOND_QUARTER, '2ND QUARTER REPORT'),
        (THIRD_QUARTER, '3RD QUARTER REPORT'),
        (FOURTH_QUARTER, 'ANNUAL BUDGET REPORT'),
        (OTHER, 'NONE OF THE ABOVE'))

    # todo:change quarter choices to commaseperatedcharacterfield
    title = models.CharField(max_length=500, verbose_name='title Of Report')
    report_type = models.CharField(
        max_length=5, choices=REPORT_TYPE_CHOICES,
        verbose_name='type Of Report', default=FIRST_REPORT)

    date = models.DateField(max_length=4, verbose_name='date Issued')
    source_of_report = models.CharField(
        max_length=500, verbose_name='source Of Report')

    source_url = models.URLField(
        max_length=500, blank=True, null=True,
        help_text='Optional', verbose_name='url To Source')

    # add report type
    def __unicode__(self):
        return '{date} {title} '.format(
            title=self.title, date=self.date)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
