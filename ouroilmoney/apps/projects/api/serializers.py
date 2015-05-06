from rest_framework import serializers
from ouroilmoney.apps.projects.models import (
    AnnualBudgetSector,
    ConfirmSector,
    AnnualBudgetProject,
    ConfirmProject,
    AbaPriorityAreas)

from ouroilmoney.apps.allocations.api.serializers import (
    AnnualBudgetAllocationSerializer,
    ConfirmAllocationSerializer)

from ouroilmoney.utils.api.serializers import MinistrySerializer


class ConfirmSectorSerializer(serializers.ModelSerializer):
    allocation = ConfirmAllocationSerializer()

    class Meta:
        model = ConfirmSector
        fields = ('amount', 'currency', 'annual_budget_sector', 'allocation', 'currency')


class AbaPriorityAreasSerializer(serializers.ModelSerializer):
    abfa = AnnualBudgetAllocationSerializer()

    class Meta:
        model = AbaPriorityAreas
        fields = ('amount', 'currency', 'title', 'abfa')


class AnnualBudgetSectorSerializer(serializers.ModelSerializer):
    allocation = AnnualBudgetAllocationSerializer()
    othersectors = ConfirmSectorSerializer(many=True)

    class Meta:
        model = AnnualBudgetSector
        fields = ('title', 'amount', 'currency', 'allocation', 'othersectors')


class AnnualBudgetSectorProjectSerializer(serializers.ModelSerializer):
    allocation_report_date = serializers.Field(source='allocation_date')

    class Meta:
        model = AnnualBudgetSector
        fields = ('allocation_report_date',)


class ConfirmProjectSerializer(serializers.ModelSerializer):
    sector = ConfirmSectorSerializer()

    class Meta:
        model = ConfirmProject
        fields = (
            'id', 'amount', 'currency', 'sector', 'created', 'modified',
            'image')


class ConfirmAnnualProjectSerializer(serializers.ModelSerializer):
    other_allocation_report_date = serializers.Field(source='other_allocation_date')


    class Meta:
        model = ConfirmProject
        fields = ('other_allocation_report_date',)


class AnnualBudgetProjectSerializer(serializers.ModelSerializer):
    sector = AnnualBudgetSectorProjectSerializer()
    otherprojects = ConfirmAnnualProjectSerializer()
    ministry = MinistrySerializer()

    class Meta:
        model = AnnualBudgetProject
        fields = (
            'id', 'title','amount','currency', 'sector','otherprojects',
            'created','modified','regions', 'town','ministry')


class ProjectListSerializer(serializers.ModelSerializer):
    sector_title = serializers.CharField()

    class Meta:
        model = AnnualBudgetProject
        fields = ('id', 'title', 'sector_title')
