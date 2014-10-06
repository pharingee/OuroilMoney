from django.db import models

# Create your models here.


class TimeStampedPublishModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name='publish')
    summary = models.TextField(
        null=True, blank=True,
        help_text='Please copy and past summary of Report here.\n Optional')

    class Meta:
        abstract = True
