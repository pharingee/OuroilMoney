from django.db import models
from ouroilmoney.utils.models import TimeStampedPublishModel


class KnowledgeHub(TimeStampedPublishModel):
    # todo:change quarter choices to commaseperatedcharacterfield
    GOVERNMENT = 'GOVERNMENT'
    PIAC = "PIAC"
    CIVIL_SOCIETY = "CIVIL SOCIETY"
    CATEGORIES = (
        (PIAC, PIAC),
        (GOVERNMENT, GOVERNMENT),
        (CIVIL_SOCIETY, CIVIL_SOCIETY))

    title = models.CharField(max_length=500, verbose_name='title Of Report')

    date = models.DateField(max_length=4, verbose_name='date Released')

    category = models.CharField(max_length=14, choices=CATEGORIES)

    subcategory = models.CharField(max_length= 500, verbose_name= "subcategory",null=True, blank=True)

    document = models.FileField(
        upload_to='documents/%Y/%m/%d/',
        verbose_name='upload Docs and Publications')

    def report_has_document(self):
        if self.document:
            return True
        return False

    report_has_document.boolean = True

    def get_document(self):
        if self.document:
            return self.document.url
        return None
