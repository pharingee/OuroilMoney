from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator

from ouroilmoney.apps.projects.models import AnnualBudgetProject


def set_sorter(sort_by, sorter):
    for sort in sorter:
        if sort == sort_by:
            sorter[sort] = 'active'
        else:
            sorter[sort] = ''
    return sorter


def project(request, project_id):
    project = AnnualBudgetProject.objects.get(id=int(project_id))
    return render(request, 'project.html', {'project': project})


def projects(request):
    sort_by = request.GET.get('sort', 'sector')
    sector = request.GET.get('sector', None)
    search = request.GET.get('search', None)
    page = request.GET.get('page', '1')

    projects = AnnualBudgetProject.objects.all().order_by('sector')
    sorter = {
        'sector': 'active',
        'town': '',
        'ministry': ''
    }

    if sort_by:
        projects = projects.order_by(sort_by)
        sorter = set_sorter(sort_by, sorter)

    if sector:
        projects = projects.filter(sector__title=sector)

    if search:
        projects = projects.filter(
            Q(sector__title__icontains=search) |
            Q(ministry__ministry__icontains=search) |
            Q(town__icontains=search) |
            Q(title__icontains=search)
        )

    p = Paginator(projects, 15)

    return render(
        request, 'project-list.html',
        {
            'projects': p.page(int(page)),
            'sorter': sorter,
            'search': search,
            'sector': sector,
            'page': page
        })
