from django.db import models

# Create your models here.

# Create your models here.
class AmountModel(models.Model):
    GHANACEDI = 'GHS'
    DOLLARS = '$'

    CURRENCY = ((GHANACEDI,'GHS(GHANA CEDI)'), (DOLLARS,'$ (DOLLARS)'))

    amount = models.DecimalField(decimal_places=2, max_digits=19,null=True,  blank=True)

    currency= models.CharField(max_length='5', choices=CURRENCY, default=DOLLARS)

    class Meta:
        abstract=True


class TimeStampedPublishModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name='publish')
    summary = models.TextField(
        null=True, blank=True,
        help_text='Please copy and past summary of Report here.\n Optional')

    class Meta:
        abstract = True





class Region(models.Model):
    # todo:write validations to avoid adding regions if dey already exists.
    # or if you are about to delete a region dat does not exist.
    GREATER = 'GREATER ACCRA REGION'
    ASHANTI = 'ASHANTI REGION'
    NORTHERN = 'NORTHERN REGION'
    UPPER_EAST = 'UPPER EAST REGION'
    UPPER_WEST = 'UPPER WEST REGION'
    EASTERN = 'EASTERN REGION'
    WESTERN = 'WESTERN REGION'
    CENTRAL = 'CENTRAL REGION'
    VOLTA = 'VOLTA REGION'
    BRONG_AHAFO = 'BRONG AHAFO REGION'

    REGIONS = (
        (GREATER, 'GREATER REGION'),
        (ASHANTI, 'ASHANTI REGION'),
        (NORTHERN, 'NORTHERN REGION'),
        (UPPER_WEST, 'UPPER WEST REGION'),
        (UPPER_EAST, 'UPPER EAST REGION'),
        (EASTERN, 'EASTERN REGION'),
        (WESTERN, 'WESTERN REGION'),
        (CENTRAL, 'CENTRAL REGION'),
        (VOLTA, 'VOLTA REGION'),
        (BRONG_AHAFO, 'BRONG AHAFO REGION'))

    region = models.CharField(
        max_length=20,
        verbose_name='region of Project',
        choices=REGIONS,
        blank=True,
        null=True)


    def __unicode__(self):
        return self.region


    class Meta:
        verbose_name = 'Region'
        verbose_name_plural  = "Regions"




class SmsMessage(models.Model):
    UNVERIFIED = 'unverified'
    VERIFIED = 'verified'
    DELETED = 'deleted'


    STATUS = (
    (UNVERIFIED, 'Unverified'),
    (VERIFIED, 'Verified'),
    (DELETED, 'Deleted')
)


    message = models.CharField(max_length=160)
    user = models.CharField(max_length=50)
    status = models.CharField(
        choices=STATUS, max_length=10, default=UNVERIFIED)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='publish')

    class Meta:
        verbose_name = 'Sms Message'
        verbose_name_plural = 'Sms Messages'

    def __unicode__(self):
        return self.user

    @property
    def comment(self):
        return "%s: %s" % (self.user, self.message)

    @property
    def get_status(self):
        return self.status
