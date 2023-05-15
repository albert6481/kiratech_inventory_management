from django.test import TestCase
from django.urls import reverse
from .models import Supplier, Inventory
from django.db import transaction

class TestURL(TestCase):
    
    def test_inventory_api(self):
        response = self.client.get('/api/inventory')
        self.assertEqual(response.status_code, 200)

    def test_inventory_list_page(self):
        response = self.client.get('/inventory')
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail_page(self):
        supplier = Supplier.objects.create(name='test')
        obj = Inventory.objects.create(name='test', description='create test object to test page', supplier=supplier)
        
        response = self.client.get('/inventory/' + str(obj.id))
        self.assertEqual(response.status_code, 200)

        # use rollback to undo the creation
        transaction.set_rollback(True)