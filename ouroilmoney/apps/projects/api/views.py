from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from ouroilmoney.apps.projects.models import (
    AnnualBudgetSector, ConfirmSector,
    AnnualBudgetProject, ConfirmProject)


from ouroilmoney.apps.projects.api.serializers import (
    AnnualBudgetSectorSerializer,
    ConfirmSectorSerializer,
    AnnualBudgetProjectSerializer,
    ConfirmProjectSerializer)


# todo: group projects into sectors

class AnnualBudgetSectorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Annual Budget Sector Resource

    """
    queryset = AnnualBudgetSector.objects.exclude(
        is_published=False).order_by('title')
    serializer_class = AnnualBudgetSectorSerializer

    @list_route(methods=["get"])
    def titles(self, request):
        """
        Get the titles of all sectors
        """
        title = AnnualBudgetSector.objects.values_list(
            'title', flat=True).order_by('title').distinct('title')
        return Response(title)


class ConfirmSectorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Sectors Resources from Other Reports other than the Annual Budget Reports
    """
    queryset = ConfirmSector.objects.exclude(
        is_published=False).order_by('annual_budget_sector__title')
    serializer_class = ConfirmSectorSerializer


class AnnualBudgetProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Annual Budget Report Projects Resource
    """

    queryset = AnnualBudgetProject.objects.exclude(
        is_published=False)
    serializer_class = AnnualBudgetProjectSerializer

    @list_route(methods=["get"])
    def titles(self, request):
        """
        Get the titles of all Projects
        """
        title = AnnualBudgetProject.objects.values_list(
            'title', flat=True).order_by('title').distinct('title')
        return Response(title)


class ConfirmProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Project Resources from Other Reports other than the Annual Budget Reports
    """

    queryset = ConfirmProject.objects.exclude(
        is_published=False)
    serializer_class = ConfirmProjectSerializer
