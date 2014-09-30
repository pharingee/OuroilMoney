from django.db import models
from ouroilmoney.apps.reports.models import Report


# Create your models here.
class Revenue(models.Model):
    #ABR refers to the annual budget report
    report = models.ForeignKey(
        Report, limit_choices_to={'report_type': 'ABR'}, verbose_name='choose Report')

    title = models.CharField(max_length=500, verbose_name='title Of Revenue')
    amount = models.CommaSeparatedIntegerField(max_length=40, verbose_name='amount Of Money  ')
    # todo:limit date based on the date from the revenue chosen
    year = models.IntegerField(max_length=4)

    @property
    def revenue_amount(self):
        return '${amount}'.format(amount=self.amount)

    def __unicode__(self):
        return '{title} {year} {amount}'.format(
            title=self.title, year=self.year, amount=self.amount)
