from rest_framework import serializers
from ouroilmoney.apps.projects.models import (
    AnnualBudgetSector,
    ConfirmSector,
    AnnualBudgetProject,
    ConfirmProject)

from ouroilmoney.apps.allocations.api.serializers import AnnualBudgetAllocationSerializer



class AnnualBudgetSectorSerializer(serializers.ModelSerializer):
    allocation =  AnnualBudgetAllocationSerializer()

    class Meta:
        model = AnnualBudgetSector
        fields = ('title','amount','allocation')


class ConfirmSectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmSector


class AnnualBudgetProjectSerializer(serializers.ModelSerializer):
    sector = AnnualBudgetSectorSerializer()

    class Meta:
        model = AnnualBudgetProject
        fields = ('id', 'title','amount', 'sector','created','modified')


class ConfirmProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConfirmProject
