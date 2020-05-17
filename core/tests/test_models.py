# -*- coding: utf-8 -*-
"""
Tests for core module's models.
"""
from unittest import TestCase

import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestCoreModels(TestCase):
	"""
	Class for testing core models
	"""

	def test_user(self):
		"""
		Tests for User model
		"""
		user = mixer.blend(
			'core.User', username = 'jane_doo', first_name = 'Jane', last_name = 'Doo', is_superuser = True)
		self.assertIsNotNone(user, 'Should create a User instance')
		self.assertEqual(str(user), 'jane_doo <Jane Doo>', 'Should be a jane_doo <Jane Doo> named object')
