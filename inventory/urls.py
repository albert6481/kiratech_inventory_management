# Django
from django.urls import path
from django.conf.urls import include

# DRF
from rest_framework import routers

# Local
from .views import InventoryViewSet, InventoryListView, InventoryDetailView

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'inventory', InventoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("inventory", InventoryListView, name="inventory-list"),
    path("inventory/<pk>", InventoryDetailView.as_view(template_name="inventory/inventory_detail.html"), name="inventory-detail"),
]
