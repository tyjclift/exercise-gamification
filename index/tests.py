from django.test import TestCase
from .models import *
# Create your tests here.


class UpperBodyTest(TestCase):
	def test_is_valid(self):
		test_form = UpperBodyForm(data={
			'type': 'Pushups',
			'reps': 1,
			'sets': 1,
			'date': '2021-01-01'
		})
		self.assertTrue(test_form.is_valid())
	def test_is_invalid(self):
		test_form = UpperBodyForm(data={
			'type': 'Pushups',
			'reps': -1,
			'sets': 1,
			'date': '2021-01-01'
		})
		self.assertFalse(test_form.is_valid())

class LowerBodyTest(TestCase):
	def test_is_valid(self):
		test_form = LowerBodyForm(data={
			'type': 'Squats',
			'reps': 1,
			'sets': 1,
			'date': '2021-01-01'
		})
		self.assertTrue(test_form.is_valid())
	def test_is_invalid(self):
		test_form = UpperBodyForm(data={
			'type': 'Squats',
			'reps': -1,
			'sets': 1,
			'date': '2021-01-01'
		})
		self.assertFalse(test_form.is_valid())

class CardioTest(TestCase):
	def test_is_valid(self):
		test_form = CardioForm(data={
			'type': 'Running',
			'time': 0,
			'distance': 0,
			'date': '2021-01-01'
		})
		self.assertTrue(test_form.is_valid())
	def test_is_invalid(self):
		test_form = UpperBodyForm(data={
			'type': 'Running',
			'time': -1,
			'distance': 0,
			'date': '2021-01-01'
		})
		self.assertFalse(test_form.is_valid())
