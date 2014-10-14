from rest_framework import serializers
from ouroilmoney.apps.allocations.models import (
    AnnualBudgetAllocation,
    ConfirmAllocation)


class AnnualBudgetAllocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnnualBudgetAllocation
        fields = ('id', 'report', 'title', 'amount')


class ConfirmAllocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConfirmAllocation
        fields = ('id', 'annual_budget_allocation', 'report', 'amount')
