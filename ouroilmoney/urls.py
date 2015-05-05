
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from apps.reports.api.views import (
    ReportViewSet,
    AnnualBudgetReportViewSet,
    OtherReportViewSet)
from apps.revenues.api.views import (AnnualBudgetRevenueViewSet)
from apps.liftings.api.views import LiftingViewSet
from apps.projects.api.views import (
    AnnualBudgetSectorViewSet,
    ConfirmSectorViewSet,
    AnnualBudgetProjectViewSet,
    ConfirmProjectViewSet)
from apps.allocations.api.views import (
    AnnualBudgetAllocationViewSet,
    ConfirmAllocationViewSet)
from apps.knowledgehubs.api.views import (
    KnowledgeHubViewSet)
from utils.api.views import (
    SmsMessageViewSet,
    MinistryViewset,
    OilPartnerViewset,
    OilFieldViewset)

router = DefaultRouter()
router.register(r'reports', ReportViewSet, base_name="reports")
router.register(r'annualbudgetreports', AnnualBudgetReportViewSet)
router.register(r'otherreports', OtherReportViewSet)
router.register(r'revenues', AnnualBudgetRevenueViewSet)
router.register(r'liftings', LiftingViewSet)
router.register(r'annualbudgetallocations', AnnualBudgetAllocationViewSet)
router.register(r'otherallocations', ConfirmAllocationViewSet)
router.register(r'annualbudgetsectors', AnnualBudgetSectorViewSet)
router.register(r'othersectors', ConfirmSectorViewSet)
router.register(r'annualbudgetprojects', AnnualBudgetProjectViewSet)
router.register(r'otherprojects', ConfirmProjectViewSet)
router.register(r'knowledgehubs', KnowledgeHubViewSet)
router.register(r'comments', SmsMessageViewSet)
router.register(r'ministries', MinistryViewset)
router.register(r'fields', OilFieldViewset)
router.register(r'partner', OilPartnerViewset)


urlpatterns = patterns(
    '',
    url(r'', include(admin.site.urls)),
    url(r'^api/v1.0/docs/', include('rest_framework_swagger.urls')),
    url(r'api/v1.0/', include(router.urls)),
)
