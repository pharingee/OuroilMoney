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
    ConfirmProjectSerializer,
    ProjectListSerializer)


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
        titles = AnnualBudgetProject.objects.all()
        titles = ProjectListSerializer(titles, many=True)
        return Response(titles.data)

    @list_route(methods=["get"])
    def ministry_of_communication_and_technology(self, request):
        """
        Get a list of projects under the ministry of
        communication and technology
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='CN')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_defence(self, request):
        """
        Get a list of projects under ministry of defence
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='DF')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_education_and_sports(self, request):
        """
        Get a list of projects under the ministry of education and sports
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='ES')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_energy(self, request):
        """
        Get a list of projects under the ministry of energy
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='EG')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_environment_and_science(self, request):
        """
        Get a list of projects under environment and science
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='ENS')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_finance_and_economic_planning(self, request):
        """
        Get a list of projects under ministry of finance and economic planning
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='FP')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_information(self, request):
        """
        Get a list of projects under ministry of information
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='IN')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_food_and_agriculture(self, request):
        """
        Get a list of projects under the ministry of food and agriculture
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='FAA')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_foreign_affairs(self, request):
        """
        Get a list of first of projects under the ministry of foreign affairs
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='DF')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_health(self, request):
        """
        Get a list of projects under the ministry of health
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='HT')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_justice_and_attorney_generals_department(self, request):
        """
        Get a list of projects under the ministry of
        justice and attorney general's departments
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='JS')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_lands_and_forestry_and_mines(self, request):
        """
        Get a list of projects under the ministry of lands and forestry
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='LS')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_local_government_and_rural_developement(self, request):
        """
        Get a list of projects under the ministry of local government and rural
         development
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='LG')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_mampower_youth_and_employment(self, request):
        """
        Get a list of projects under the ministry of local government
        and rural development
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='YH')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_parliamentary_affairs(self, request):
        """
        Get a list of projects under the ministry of parliamentary affairs
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='PA')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_private_sector_development(self, request):
        """
        Get a list of projects under the ministry of private sector
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='PD')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_regional_cooperation_and_nepad(self, request):
        """
        Get a list of projects under the ministry of
        regional coperation and nepad
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='RC')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_road_transport(self, request):
        """
        Get a list of projects under the ministry of road and transport
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='RT')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_tourism_and_modernization_capital_city(self, request):
        """
        Get a list of projects under the ministry of tourism
         and modernization of the capital city.
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='TM')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_trade_and_housing(self, request):
        """
        Get a list of projects under the ministry of trade and housing
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='TI')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def ministry_of_women_and_children_affairs(self, request):
        """
        Get a list of projects under the ministry of women
        and children's affairs
        """
        projects = AnnualBudgetProject.objects.filter(
            ministry__ministry='WA')

        serializer = AnnualBudgetProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ConfirmProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Project Resources from Other Reports other than the Annual Budget Reports
    """

    queryset = ConfirmProject.objects.exclude(
        is_published=False)
    serializer_class = ConfirmProjectSerializer
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100
