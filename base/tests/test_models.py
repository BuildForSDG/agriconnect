# -*- coding: utf-8 -*-
"""
This file contains the tests for models in this module.
"""
from unittest import TestCase

import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestBaseModels(TestCase):
	"""
	Class for testing base models
	"""

	def test_status(self):
		"""
		Test for Status model
		"""

		state = mixer.blend('base.Status', name = 'Active')
		self.assertIsNotNone(state, 'Should create a State instance')
		self.assertEqual(str(state), 'Active', 'Should be a Active named object')

	def test_account_type(self):
		"""
		Test for AccountType model
		"""

		account_type = mixer.blend('base.AccountType', name = 'Farmer')
		self.assertIsNotNone(account_type, 'Should create a AccountType instance')
		self.assertEqual(str(account_type), 'Farmer', 'Should be a Farmer named object')

	def test_category(self):
		"""
		Test for Category model
		"""

		category = mixer.blend('base.Category', name = 'Default')
		self.assertIsNotNone(category, 'Should create a Category instance')
		self.assertEqual(str(category), 'Default', 'Should be a Default named object')
