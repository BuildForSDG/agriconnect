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

	def setUp(self) -> None:
		self.state_active = mixer.blend('base.Status', name = 'Active')

	def test_user(self):
		"""
		Tests for User model
		"""
		user = mixer.blend(
			'core.User', username = 'jane_doo', first_name = 'Jane', last_name = 'Doo', is_superuser = True)
		self.assertIsNotNone(user, 'Should create a User instance')
		self.assertEqual(str(user), 'jane_doo <Jane Doo>', 'Should be a jane_doo <Jane Doo> named object')

	def test_post(self):
		"""
		Tests for Post model
		"""
		user = mixer.blend(
			'core.User', username = 'jane_doo', first_name = 'Jane', last_name = 'Doo', is_superuser = True)
		category = mixer.blend('base.Category', name = 'Default')
		post = mixer.blend('core.Post', title = 'Authored', user = user, category = category)
		self.assertIsNotNone(post, 'Should create a Post instance')
		self.assertEqual(str(post), 'Authored-%s(Active)' % post.category, 'Should be a properly named object')
