"""
The base models definition.
"""
import uuid

from django.db import models


class BaseModel(models.Model):
	"""
	The base model definition with which every model ought to inherit from.
	"""
	id = models.UUIDField(max_length = 100, default = uuid.uuid4, unique = True, editable = False, primary_key = True)
	date_modified = models.DateTimeField(auto_now = True)
	date_created = models.DateTimeField(auto_now_add = True)

	class Meta(object):
    		abstract = True

	def get_foreign_keys(self):
		"""
		Retrieves the foreign keys for the model. Puts the retrieved fields into a list.
		@return: The foreign keys found.
		@rtype: list
		"""
		foreign_keys = []
		try:
			for field in self._meta.fields:
				if isinstance(self._meta.get_field(field.name), models.ForeignKey):
					foreign_keys.append(field.name)
		except Exception as e:
			print('get_foreign_keys Exception: %s' % e)
		return foreign_keys

	def get_passable_fields(self):
		"""
		Meta data definition for the abstract model.
		"""
		abstract = True


class GenericBaseModel(BaseModel):
	"""
	Define repetitive fields to avoid cycles of redefining in every model.
	Contains the name and description.
	"""
	name = models.CharField(max_length = 100)
	description = models.TextField(max_length = 300, blank = True, null = True)

	class Meta(object):
		"""
		Meta data definition for the abstract model.
		"""
		abstract = True


class Status(GenericBaseModel):
	"""
	Statuses for objects lifecycle e.g. "Active", "Activation Pending", "Reversed", etc
	"""

	def __str__(self):
		"""
		Returns the name for the Status.
		@return: Name of Status
		"""
		return '%s' % self.name

	class Meta(object):
		"""
		Meta data definition for the model.
		"""
		ordering = ('name',)
		unique_together = ('name',)
		verbose_name_plural = 'statuses'

	@classmethod
	def default_status(cls):
		"""
		The default Active state.
		@return: The active state, if it exists, or None if it doesn't exist.
		@rtype: uuid | str | None
		"""
		try:
			state = cls.objects.get(name = 'Active')
			return state.id
		except Exception as x:
			print('default_status Exception: %s' % x)
		return None

	@classmethod
	def disabled_status(cls):
		"""
		The default Disabled state.
		@return: The disabled state, if it exists, or None if it doesn't exist.
		@rtype: uuid | str | None
		"""
		try:
			state = cls.objects.get(name = 'Disabled')
			return state
		except Exception as x:
			print('disabled_status Exception: %s' % x)
		return None


class AccountType(GenericBaseModel):
	"""
	A user's account type e.g. Farmer, Expert
	"""
	status = models.ForeignKey(Status, on_delete = models.PROTECT)

	def __str__(self):
		"""
		Returns the name for the AccountType.
		@return: Name of AccountType
		"""
		return '%s' % self.name

	class Meta(object):
		"""
		Meta data definition for the model.
		"""
		ordering = ('name',)
		unique_together = ('name',)


class Category(GenericBaseModel):
	"""
	A post's account type e.g. Default,
	"""
	status = models.ForeignKey(Status, on_delete = models.PROTECT)

	def __str__(self):
		"""
		Returns the name for the category.
		@return: Name of category
		"""
		return '%s' % self.name

	class Meta(object):
		"""
		Meta data definition for the model.
		"""
		ordering = ('name',)
		unique_together = ('name',)
		verbose_name_plural = 'categories'

	@classmethod
	def default_category(cls):
		"""
		The Default category.
		@return: The Default category, if it exists, or None if it doesn't exist.
		@rtype: uuid | str | None
		"""
		try:
			category = cls.objects.get(name = 'Default')
			return category.id
		except Exception as x:
			print('default_category Exception: %s' % x)
		return None

class Reaction(GenericBaseModel):
	"""
	A user's reaction
	"""
	status = models.ForeignKey(Status, on_delete = models.PROTECT)

	def __str__(self):
		return '%s' % self.name