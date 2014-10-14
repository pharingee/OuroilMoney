from rest_framework import viewsets
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


class ConfirmSectorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConfirmSector.objects.exclude(
        is_published=False).order_by(' annual_budget_sector__title')
    serializer_class = ConfirmSectorSerializer


class AnnualBudgetProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnnualBudgetProject.objects.exclude(
        is_published=False)
    serializer_class = AnnualBudgetProjectSerializer


class ConfirmProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConfirmProject.objects.exclude(
        is_published=False)
    serializer_class = ConfirmProjectSerializer
