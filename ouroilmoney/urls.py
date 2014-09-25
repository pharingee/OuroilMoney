from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers  import DefaultRouter

# ViewSet
from apps.reports.api.views import ReportsViewSet


router = DefaultRouter()
router.register(r'reports', ReportsViewSet)

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'', include(admin.site.urls)),
    url(r'api/v1.0/', include(router.urls))
)
