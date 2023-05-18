from rest_framework.routers import DefaultRouter
from django.urls import include, path

from partner.views import AllPartnerView, PartnerDetailsView

router = DefaultRouter()
router.register("partner_detail", PartnerDetailsView, basename="course_detail")
router.register("partner_list", AllPartnerView, basename="All_partner")

urlpatterns = [
    path('', include(router.urls)),

]
