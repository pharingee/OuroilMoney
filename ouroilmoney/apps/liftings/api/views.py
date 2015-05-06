from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from ouroilmoney.apps.liftings.models import Lifting
from ouroilmoney.apps.liftings.api.serializers import LiftingSerializer


class LiftingViewSet(viewsets.ReadOnlyModelViewSet):
    """
    lifting Resource
    Liftings are from other quarter reports released by the governments.
    """

    queryset = Lifting.objects.exclude(is_published=False)
    serializer_class = LiftingSerializer
