from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'ouroilmoney.frontend.views.general.home', name='home'),

    url(r'^data/$', 'ouroilmoney.frontend.views.general.data', name='data'),
    url(r'^comments/$', 'ouroilmoney.frontend.views.general.comments',
        name='comments'),
    url(r'^resources/$', 'ouroilmoney.frontend.views.general.resources',
        name='resources'),

    url(r'^data/revenues/(?P<year>[0-9]{4})/$',
        'ouroilmoney.frontend.views.data.revenues', name='revenues'),
    url(r'^data/allocations/(?P<year>[0-9]{4})/$',
        'ouroilmoney.frontend.views.data.allocations', name='allocations'),
    url(r'^data/liftings/(?P<year>[0-9]{4})/$',
        'ouroilmoney.frontend.views.data.liftings', name='liftings'),
    url(r'^data/abfa-priority/$',
        'ouroilmoney.frontend.views.data.abfa_priority', name='abfa_priority'),
    url(r'^data/abfa-sectors/$',
        'ouroilmoney.frontend.views.data.abfa_sectors', name='abfa_sectors'),

    url(r'^resources/knowledgehub/$',
        'ouroilmoney.frontend.views.resources.knowledgehub',
        name='knowledgehub'),
    url(r'^resources/calendar/$',
        'ouroilmoney.frontend.views.resources.report_calendar',
        name='calendar'),

    url(r'^projects/(?P<project_id>[0-9]+)/$',
        'ouroilmoney.frontend.views.projects.project', name='project'),
    url(r'^projects/$',
        'ouroilmoney.frontend.views.projects.projects', name='projects')
)
