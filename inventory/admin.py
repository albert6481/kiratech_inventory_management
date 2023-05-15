from django.contrib import admin

from .models import Supplier, Inventory

admin.site.site_header = 'Inventory Management System'

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering     = ('id', )


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'notes', 'stock', 'availability', 'supplier_name')
    list_filter  = ('availability', )
    ordering     = ('id', 'stock', 'name')

    def supplier_name(self, obj):
        return obj.supplier.name

    # Rename field name
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['supplier'].label_from_instance = lambda inst: "{}. {}".format(inst.id, inst.name)

        return form