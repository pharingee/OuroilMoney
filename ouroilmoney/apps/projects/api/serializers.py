from rest_framework import serializers
from ouroilmoney.apps.projects.models import (
    AnnualBudgetSector,
    ConfirmSector,
    AnnualBudgetProject,
    ConfirmProject)

from ouroilmoney.apps.allocations.api.serializers import (
    AnnualBudgetAllocationSerializer,
    ConfirmAllocationSerializer)


class ConfirmSectorSerializer(serializers.ModelSerializer):
    allocation = ConfirmAllocationSerializer()

    class Meta:
        model = ConfirmSector
        fields = ('amount','currency','annual_budget_sector','allocation', 'currency')



class AnnualBudgetSectorSerializer(serializers.ModelSerializer):
    allocation =  AnnualBudgetAllocationSerializer()
    othersectors = ConfirmSectorSerializer(many=True)

    class Meta:
        model = AnnualBudgetSector
        fields = ('title','amount', 'currency','allocation','othersectors')


class ConfirmProjectSerializer(serializers.ModelSerializer):
    sector = ConfirmSectorSerializer()

    class Meta:
        model = ConfirmProject
        fields = (
            'id', 'amount', 'currency','sector','created','modified',
            'image')


class AnnualBudgetProjectSerializer(serializers.ModelSerializer):
    sector = AnnualBudgetSectorSerializer()
    otherprojects = ConfirmProjectSerializer(many=True)

    class Meta:
        model = AnnualBudgetProject
        fields = (
            'id', 'title','amount','currency', 'sector','otherprojects',
            'created','modified','region', 'town')


class ProjectListSerializer(serializers.ModelSerializer):
    sector_title = serializers.CharField()

    class Meta:
        model = AnnualBudgetProject
        fields = ('id', 'title', 'sector_title')
