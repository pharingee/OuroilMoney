from rest_framework import serializers
from ouroilmoney.apps.revenues.models import AnnualBudgetReportRevenue


class AnnualBudgetRevenueSerializer(serializers.ModelSerializer):
    amount = serializers.Field(source='revenue_amount')

    class Meta:
        model = AnnualBudgetReportRevenue
        fields = ('id', 'title', 'amount', 'year')
