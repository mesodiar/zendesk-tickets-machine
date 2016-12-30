from django.test import TestCase
from ..models import Sheet

class SheetTest(TestCase):
	def test_save_sheet(self):
		sheet = Sheet()
		sheet.name = 'Pre-Production'
		sheet.slug = 'pre-production'
		sheet.save()

		sheet = Sheet.objects.last()

		self.assertEqual(sheet.name, 'Pre-Production')
		self.assertEqual(sheet.slug, 'pre-production')

	def test_sheet_should_represent_name_by_default(self):
		sheet = Sheet.objects.create(
			name='Pre-Production',
			slug='pre-production'
		)
		self.assertEquals(sheet.__str__(), 'Pre-Production')