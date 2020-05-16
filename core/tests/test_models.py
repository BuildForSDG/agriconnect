# -*- coding: utf-8 -*-
"""
Tests for core module's models.
"""

import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestCoreModels(object):
	"""
	Class for testing core models
	"""

	def test_user(self):
		"""
		Tests for User model
		"""

		user = mixer.blend('core.User', username = 'jane_doo', first_name = 'Jane', last_name = 'Doo')
		assert user is not None, 'Should create a User instance'
		assert str(user) == 'jane_doo <Jane Doo>', 'Should be a jane_doo named object'
