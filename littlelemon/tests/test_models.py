from django.test import TestCase
from restaurant.models import MenuItem

class MenuTest(TestCase):
	def test_get_item(self):
		item = MenuItem.objects.create(title="IceCream", price=80, inventory=3)
		self.assertEqual(item, "IceCream")
		