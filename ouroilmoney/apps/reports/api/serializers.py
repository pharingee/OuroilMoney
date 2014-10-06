from rest_framework import serializers
from ouroilmoney.apps.reports.models import AnnualBudgetReport


class AnnualBudgetReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualBudgetReport
