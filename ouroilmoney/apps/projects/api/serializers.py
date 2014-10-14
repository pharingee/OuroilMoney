from rest_framework import serializers
from ouroilmoney.apps.projects.models import (
    AnnualBudgetSector,
    ConfirmSector,
    AnnualBudgetProject,
    ConfirmProject)

from ouroilmoney.apps.allocations.api.serializers import (
    AnnualBudgetAllocationSerializer,
    ConfirmAllocationSerializer)



class AnnualBudgetSectorSerializer(serializers.ModelSerializer):
    allocation =  AnnualBudgetAllocationSerializer()

    class Meta:
        model = AnnualBudgetSector
        fields = ('title','amount','allocation')


class ConfirmSectorSerializer(serializers.ModelSerializer):
    allocation =  ConfirmAllocationSerializer()

    class Meta:
        model = ConfirmSector
        fields = ('amount','annual_budget_sector','allocation')


class AnnualBudgetProjectSerializer(serializers.ModelSerializer):
    sector = AnnualBudgetSectorSerializer()

    class Meta:
        model = AnnualBudgetProject
        fields = ('id', 'title','amount', 'sector','created','modified')


class ConfirmProjectSerializer(serializers.ModelSerializer):
    sector = ConfirmSectorSerializer()

    class Meta:
        model = ConfirmProject
        fields = ('id', 'amount', 'sector','created','modified')

