# Django
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.detail import DetailView

# DRF
from rest_framework import viewsets

# 3rd Party
from django_filters.rest_framework import DjangoFilterBackend

# Local
from .models import Inventory
from .serializers import InventorySerializer

'''
API
'''
class InventoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions for Inventory model.
    """
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']



'''
FRONTEND
'''
def InventoryListView(request):
    return render(request, 'inventory/inventory_list.html')


class InventoryDetailView(DetailView):
    model = Inventory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context