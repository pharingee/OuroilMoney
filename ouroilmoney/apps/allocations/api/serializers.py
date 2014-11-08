from rest_framework import serializers
from ouroilmoney.apps.allocations.models import (
    AnnualBudgetAllocation,
    ConfirmAllocation)
from ouroilmoney.apps.reports.api.serializers import (
    AnnualBudgetReportSerializer, OtherReportSerializer)

class ConfirmAllocationSerializer(serializers.ModelSerializer):
    report = OtherReportSerializer()
    allocation_type = serializers.SerializerMethodField('type')

    def type(self, obj):
        return 'Other Report Allocation'

    class Meta:
        model = ConfirmAllocation
        fields = (
            'id', 'allocation_type',
            'annual_budget_allocation',
            'report', 'amount','currency','created', 'modified')


class AnnualBudgetAllocationSerializer(serializers.ModelSerializer):
    report = AnnualBudgetReportSerializer()
    allocation_type = serializers.SerializerMethodField('type')
    otherallocations = ConfirmAllocationSerializer(many=True)

    def type(self, obj):
        return 'Annual Budget Report Allocation'



    class Meta:
        model = AnnualBudgetAllocation
        fields = (
            'id', 'report', 'title',
            'allocation_type','otherallocations',
            'amount', 'currency','created',
            'modified',)


