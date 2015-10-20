# from sets import Set
from django.shortcuts import render
from django.utils import timezone

from ouroilmoney.apps.knowledgehubs.models import KnowledgeHub
from ouroilmoney.apps.reports.models import CalendarOfReport


def report_calendar(request):
    calendar = CalendarOfReport.objects.filter(date__gte=timezone.now())
    return render(request, 'report-calendar.html', {'calendar': calendar})


def knowledgehub(request):
    knowledgehub = KnowledgeHub.objects.all()
    subcategories = {}
    for knowledge in knowledgehub:
        if knowledge.subcategory:
            print knowledge.category, knowledge.subcategory.subcategory
            try:
                subcategories[knowledge.category][
                    knowledge.subcategory.subcategory].append(knowledge)
            except KeyError:
                if subcategories.get(knowledge.category):
                    subcategories[knowledge.category][
                        knowledge.subcategory.subcategory] = []
                else:
                    subcategories[knowledge.category] = {}
                subcategories[knowledge.category][
                    knowledge.subcategory.subcategory] = [knowledge]
        else:
            try:
                subcategories[knowledge.category]['all'].append(knowledge)
            except KeyError:
                subcategories[knowledge.category] = {
                    'all': [knowledge]
                }

    print subcategories

    return render(
        request, 'knowledgehub.html', {'subcategories': subcategories})
