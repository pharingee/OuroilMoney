from django.db import models

# Create your models here.


class Reports(models.Model):
    FIRST_QUARTER = '1st Quarter Report'
    SECOND_QUARTER = '2nd Quater Report'
    THIRD_QUARTER = '3rd Quater Report'
    FOURTH_QUARTER = '4th Quarter Report'
    FIRST_REPORT = 'ANNUAL BUDGET REPORT'
    OTHER = 'None of the above'

    REPORT_TYPE_CHOICES = (
        ('1Q', FIRST_QUARTER),
        ('2Q', SECOND_QUARTER),
        ('3Q', THIRD_QUARTER),
        ('4Q', FOURTH_QUARTER),
        ('YR', FIRST_REPORT),
        ('NONE OF THE ABOVE', OTHER))

    # todo:change quarter choices to commaseperatedcharacterfield
    title = models.CharField(max_length=500)
    summary = models.TextField()
    report_type = models.CharField(max_length=2, choices=REPORT_TYPE_CHOICES)
    date = models.DateField(max_length=4)
    source = models.CharField(max_length=500)
    source_url = models.URLField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return '{year} {title} '.format(title=self.title, year=self.year)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
