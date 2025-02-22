from django.urls import path, include
from rest_framework.routers import DefaultRouter

from electrohub.apps import ElectrohubConfig
from electrohub.views import CompanyViewSet, ProductViewSet, ContactsViewSet

app_name = ElectrohubConfig.name

router = DefaultRouter()
router.register(r"companies", CompanyViewSet, basename="companies")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"contacts", ContactsViewSet, basename="contacts")

urlpatterns = [
    path("", include(router.urls)),
]