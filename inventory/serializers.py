# Django
from django.db import transaction
from django.contrib.auth import login
from django.conf import settings
from django.contrib.auth.models import Group

# DRF
from rest_framework import serializers

# Local
from .models import Supplier, Inventory


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name']


class InventorySerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only = True)

    class Meta:
        model = Inventory
        fields = ['id', 'name', 'description', 'notes', 'stock', 'availability', 'supplier']

    
