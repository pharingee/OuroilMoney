from sets import Set

from django.shortcuts import render

from ouroilmoney.apps.revenues.models import AnnualBudgetReportRevenue
from ouroilmoney.apps.projects.models import AnnualBudgetProject


def home(request):
    revenue_objects = AnnualBudgetReportRevenue.objects.all()
    projects = AnnualBudgetProject.objects.all()[:5]
    revenues = {}
    years = Set([])
    total = AnnualBudgetReportRevenue.revenue_objects.totalRevenue()
    for revenue in revenue_objects:
        years.add(revenue.year)
        try:
            revenues[revenue.title][revenue.year] = float(revenue.amount)
        except KeyError:
            revenues[revenue.title] = {}
            revenues[revenue.title][revenue.year] = float(revenue.amount)
    return render(
        request, 'index.html',
        {
            'revenues': revenues,
            'years': years,
            'total': total,
            'projects': projects
        })
