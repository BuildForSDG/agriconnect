"""
The core module models
"""
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel, AccountType, Status, Category, Reaction
from core.validators import PhoneNumberValidator


class User(BaseModel, AbstractUser):
	"""
	The user customized from Django's default user.
	"""
	phone_number_validator = PhoneNumberValidator()

	GENDER_CHOICES = [
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Prefer not to Say'),
	]

	other_name = models.CharField(_('other name'), max_length = 100, null = True, blank = True)
	phone_number = models.CharField(
		_('phone number'), max_length = 20, validators = [phone_number_validator], null = True, blank = True)
	gender = models.CharField(max_length = 1, choices = GENDER_CHOICES, default = 'O')
	bio = models.TextField(max_length = 2000, null = True, blank = True)
	profile_image_url = models.URLField(max_length = 150, null = True, blank = True)
	account_type = models.ForeignKey(AccountType, on_delete = models.PROTECT, null = True, blank = True)
	status = models.ForeignKey(
		Status, on_delete = models.PROTECT, null = True, blank = True, default = Status.default_status)

	def __str__(self):
		"""
		Returns the username, first name and last name combinations.
		@return: Name repr for the user.
		"""
		if self.first_name or self.last_name:
			names = ' <%s %s>' % (self.first_name or '', self.last_name or '')
		else:
			names = ''
		return '%s%s' % (self.username, names)

	def full_name(self):
		"""
		Returns the full name of the user.
		@return: Full Name of the user.
		"""
		return '%s %s %s' % (self.first_name or '', self.last_name or '', self.other_name or '')

	def clean(self):
		"""
		Runs cleaning logic for inputs before saving the entry.
		@return: Nothing
		"""
		errors = dict()
		if not self.is_superuser:
			if not self.account_type_id:
				errors['account_type'] = 'Account type MUST be defined for non superuser.'
			if not self.status_id:
				errors['status'] = 'Status MUST be defined for non superuser.'

		if errors:
			raise ValidationError(errors)
		super(User, self).clean()

	def save(self, *args, **kwargs):
		"""
		Runs before save logic for inputs before saving the entry.
		@return: Nothing
		"""
		errors = dict()
		if not self.is_superuser:
			if not self.account_type_id:
				errors['account_type'] = 'Account type MUST be defined for non superuser.'
			if not self.status_id:
				errors['status'] = 'Status MUST be defined for non superuser.'

		if errors:
			raise ValidationError(errors)
		super(User, self).save(*args, **kwargs)


class Post(BaseModel):
	"""
	The posts model for storing the posts by users.
	"""
	title = models.CharField(_('title'), max_length = 100, null = True, blank = True)
	content = models.TextField(max_length = 5000)
	excerpt = models.TextField(max_length = 300, null = True, blank = True)
	user = models.ForeignKey(User, on_delete = models.PROTECT)
	slug = models.CharField(max_length = 255, null = True, blank = True)
	featured = models.BooleanField(default = False)
	category = models.ForeignKey(Category, default = Category.default_category, on_delete = models.PROTECT)
	parent = models.ForeignKey('self', on_delete = models.SET_NULL, null = True, blank = True)
	priority = models.DecimalField(max_digits = 25, decimal_places = 4, default = 0.0000)
	tags = models.TextField(max_length = 355, null = True, blank = True)
	comments_count = models.IntegerField(default = 0)
	reactions_count = models.IntegerField(default = 0)
	password = models.CharField(max_length = 200, null = True, blank = True)
	status = models.ForeignKey(Status, default = Status.default_status, on_delete = models.PROTECT)

	def __str__(self):
		"""
		The string repr of the object.
		@return: String representation of the instance.
		@rtype: str
		"""
		return '%s-%s(%s)' % (self.title, self.category, self.status)

class PostReaction(BaseModel):
	"""
	The post reaction model for storing users reactions to posts
	"""
	post = models.ForeignKey(Post, on_delete=models.PROTECT)
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	reaction = models.ForeignKey(Reaction, on_delete=models.PROTECT)
	status = models.ForeignKey(Status, on_delete=models.PROTECT)

	def __str__(self):
		"""
		The string repr of the object.
		@return: String representation of the instance.
		@rtype: str
		"""
		return '%s-%s' % (self.post, self.reaction)
