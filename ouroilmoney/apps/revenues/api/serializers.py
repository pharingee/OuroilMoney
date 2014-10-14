from rest_framework import serializers
from ouroilmoney.apps.revenues.models import AnnualBudgetReportRevenue

class AnnualBudgetRevenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnnualBudgetReportRevenue
        fields = ('id', 'title', 'amount', 'year')
