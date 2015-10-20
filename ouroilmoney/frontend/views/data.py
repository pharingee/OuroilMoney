from sets import Set

from django.shortcuts import render

from ouroilmoney.apps.revenues.models import AnnualBudgetReportRevenue
from ouroilmoney.apps.allocations.models import AnnualBudgetAllocation
from ouroilmoney.apps.liftings.models import Lifting
from ouroilmoney.apps.projects.models import AbaPriorityAreas
from ouroilmoney.apps.projects.models import AnnualBudgetSector


def revenues(request, year):
    revenue_objects = AnnualBudgetReportRevenue.objects.all()
    revenues = {}
    years = Set([])
    total = 0
    for revenue in revenue_objects:
        years.add(revenue.year)
        if revenue.year == int(year):
            revenues[revenue.title] = float(revenue.amount)
            total += float(revenue.amount)

    return render(
        request, 'revenues.html',
        {
            'monies': revenues,
            'years': years,
            'total': total,
            'year': int(year),
            'type': 'Revenue'
        })


def allocations(request, year):
    allocation_objects = AnnualBudgetAllocation.objects.all()
    allocations = {}
    years = Set([])
    total = 0
    for allocation in allocation_objects:
        years.add(allocation.report.date.year)
        if allocation.report.date.year == int(year):
            allocations[allocation.title] = float(
                allocation.amount.replace(',', ''))
            total += float(allocation.amount.replace(',', ''))

    return render(
        request, 'allocations.html',
        {
            'monies': allocations,
            'years': years,
            'total': total,
            'year': int(year),
            'type': 'Allocation'
        })


def liftings(request, year):
    lifting_objects = Lifting.objects.all()
    liftings = {}
    years = Set([])
    total = 0
    for lifting in lifting_objects:
        years.add(lifting.date.year)
        if lifting.date.year == int(year):
            liftings[lifting.partner] = (
                float(lifting.volume_of_lifting) *
                float(lifting.selling_price)
            )
            total += (
                float(lifting.volume_of_lifting) *
                float(lifting.selling_price)
            )

    return render(
        request, 'liftings.html',
        {
            'monies': liftings,
            'years': years,
            'total': total,
            'year': int(year),
            'type': 'Lifting'
        })


def abfa_priority(request):
    abfa_objects = AbaPriorityAreas.objects.all()
    abfas = {}
    years = Set([])
    for abfa in abfa_objects:
        years.add(abfa.abfa.report.date.year)
        try:
            abfas[abfa.title][abfa.abfa.report.date.year] = abfa.amount
        except KeyError:
            abfas[abfa.title] = {}
            abfas[abfa.title][abfa.abfa.report.date.year] = abfa.amount

    return render(
        request, 'abfa-priority.html',
        {
            'abfas': abfas,
            'years': years
        }
    )


def abfa_sectors(request):
    abfas = AnnualBudgetSector.objects.all().order_by(
        'title').distinct('title')
    return render(request, 'abfa-sectors.html', {'abfas': abfas})
