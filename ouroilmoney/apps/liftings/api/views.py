from rest_framework import viewsets
from ouroilmoney.apps.liftings.models import Lifting
from ouroilmoney.apps.liftings.api.serializers import LiftingSerializer


class LiftingViewSet(viewsets.ReadOnlyModelViewSet):
        queryset = Lifting.objects.exclude(is_published=False)
        serializer_class = LiftingSerializer
