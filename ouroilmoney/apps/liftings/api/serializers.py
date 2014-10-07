from rest_framework import serializers
from ouroilmoney.apps.liftings.models import Lifting


class LiftingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lifting
