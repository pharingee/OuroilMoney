from sets import Set

from django.shortcuts import render
from django.core.paginator import Paginator

from ouroilmoney.apps.revenues.models import AnnualBudgetReportRevenue
from ouroilmoney.apps.projects.models import AnnualBudgetProject
from ouroilmoney.utils.models import SmsMessage


def home(request):
    revenue_objects = AnnualBudgetReportRevenue.objects.all()
    projects = AnnualBudgetProject.objects.all()[:8]
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


def data(request):
    return render(request, 'data.html')


def resources(request):
    return render(request, 'resources.html')


def comments(request):
    page = request.GET.get('page', '1')
    comments = SmsMessage.objects.filter(
        is_published=True, status='verified')
    p = Paginator(comments, 25)
    return render(
        request, 'comments.html',
        {'comments': p.page(int(page)), 'page': page})
