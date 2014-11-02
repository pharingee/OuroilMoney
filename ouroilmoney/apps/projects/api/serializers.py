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
    allocation =  ConfirmAllocationSerializer()

    class Meta:
        model = ConfirmSector
        fields = ('amount','annual_budget_sector','allocation')



class AnnualBudgetSectorSerializer(serializers.ModelSerializer):
    allocation =  AnnualBudgetAllocationSerializer()
    othersectors  = ConfirmSectorSerializer(many=True)

    class Meta:
        model = AnnualBudgetSector
        fields = ('title','amount','allocation','othersectors')


class ConfirmProjectSerializer(serializers.ModelSerializer):
    sector = ConfirmSectorSerializer()

    class Meta:
        model = ConfirmProject
        fields = ('id', 'amount', 'sector','created','modified')




class AnnualBudgetProjectSerializer(serializers.ModelSerializer):
    sector = AnnualBudgetSectorSerializer()
    otherprojects = ConfirmProjectSerializer(many=True)

    class Meta:
        model = AnnualBudgetProject
        fields = ('id', 'title','amount', 'sector','otherprojects','created','modified')


