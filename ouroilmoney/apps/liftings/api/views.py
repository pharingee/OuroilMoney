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

    @list_route(methods=["get"])
    def jubilee_partners(self, request):
        """
        Get liftings related to jubilee
        """
        jubilee_partners = Lifting.objects.filter(partner='GJ')
        serializer = LiftingSerializer(jubilee_partners, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ten_partners(self, request):
        """
        Get liftings related to jubilee
        """
        ten_partners = Lifting.objects.filter(partner='TN')
        serializer = LiftingSerializer(ten_partners, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def other_partners(self, request):
            """
            Get lifting related to other partners
            """
            other_partners = Lifting.objects.exclude(partner='GJ')
            serializer = LiftingSerializer(other_partners,many=True)
            return Response(serializer.data)
