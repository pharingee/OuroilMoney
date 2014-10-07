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
    class Meta:
        model = AnnualBudgetProject

class ConfirmProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmProject