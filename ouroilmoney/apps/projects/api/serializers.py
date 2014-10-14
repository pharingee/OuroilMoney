from rest_framework import serializers
from ouroilmoney.apps.projects.models import AnnualBudgetSector
from ouroilmoney.apps.projects.models import ConfirmSector
from ouroilmoney.apps.projects.models import AnnualBudgetProject
from ouroilmoney.apps.projects.models import ConfirmProject


class AnnualBudgetSectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualBudgetSector


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
