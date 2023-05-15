from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name        = "Supplier"
        verbose_name_plural = "Suppliers"
        db_table            = 'supplier'


class Inventory(models.Model):
    supplier     = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    name         = models.CharField(max_length=255)
    description  = models.CharField(max_length=255, null=True, blank=True)
    notes        = models.TextField(null=True, blank=True)
    stock        = models.IntegerField(default=0)
    availability = models.BooleanField(default=True)

    class Meta:
        verbose_name        = "Inventory"
        verbose_name_plural = "Inventories"
        db_table            = 'inventory'
