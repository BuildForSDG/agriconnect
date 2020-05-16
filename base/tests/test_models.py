# -*- coding: utf-8 -*-
"""
This file contains the tests for models in this module.
"""

import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestBaseModels(object):
	"""
	Class for testing base models
	"""

	def test_status(self):
		"""
		Test for Status model
		"""

		state = mixer.blend('base.Status', name = 'Active')
		assert state is not None, 'Should create a State instance'
		assert str(state) == 'Active', 'Should be a Active named object'

	def test_account_type(self):
		"""
		Test for AccountType model
		"""

		account_type = mixer.blend('base.AccountType', name = 'Farmer')
		assert account_type is not None, 'Should create a AccountType instance'
		assert str(account_type) == 'Farmer', 'Should be a Farmer named object'

	def test_category(self):
		"""
		Test for Category model
		"""

		category = mixer.blend('base.Category', name = 'Default')
		assert category is not None, 'Should create a Category instance'
		assert str(category) == 'Default', 'Should be a Default named object'
