from rest_framework import serializers
from ouroilmoney.apps.reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
