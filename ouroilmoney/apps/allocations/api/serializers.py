from rest_framework import serializers
from ouroilmoney.apps.allocations.models import (
    AnnualBudgetAllocation,
    ConfirmAllocation)
from ouroilmoney.apps.reports.api.serializers import (
    AnnualBudgetReportSerializer, OtherReportSerializer)


class AnnualBudgetAllocationSerializer(serializers.ModelSerializer):
    report = AnnualBudgetReportSerializer()

    class Meta:
        model = AnnualBudgetAllocation
        fields = ('id', 'report', 'title', 'amount', 'created', 'modified')


class ConfirmAllocationSerializer(serializers.ModelSerializer):
    report = OtherReportSerializer()

    class Meta:
        model = ConfirmAllocation
        fields = ('id', 'annual_budget_allocation', 'report', 'amount')
