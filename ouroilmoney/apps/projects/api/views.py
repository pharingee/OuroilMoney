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


class AnnualBudgetSectorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnnualBudgetSector.objects.exclude(
        is_published=False).order_by('title')
    serializer_class = AnnualBudgetSectorSerializer

    @list_route(methods=["get"])
    def titles(self, request):
        title = AnnualBudgetSector.objects.values_list(
            'title', flat=True).order_by('title').distinct('title')
        return Response(title)


class ConfirmSectorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConfirmSector.objects.exclude(
        is_published=False).order_by('annual_budget_sector__title')
    serializer_class = ConfirmSectorSerializer


class AnnualBudgetProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnnualBudgetProject.objects.exclude(
        is_published=False)
    serializer_class = AnnualBudgetProjectSerializer

    @list_route(methods=["get"])
    def titles(self, request):
        title = AnnualBudgetProject.objects.values_list(
            'title', flat=True).order_by('title').distinct('title')
        return Response(title)


class ConfirmProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConfirmProject.objects.exclude(
        is_published=False)
    serializer_class = ConfirmProjectSerializer
