"""
The core module models
"""
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel, AccountType, Status
from core.validators import PhoneNumberValidator


class User(BaseModel, AbstractUser):
	"""The user customized from Django's default user."""
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
	status = models.ForeignKey(Status, on_delete = models.PROTECT, null = True, blank = True)

	def __str__(self):
		if self.first_name or self.last_name:
			names = ' <%s %s>' % (self.first_name or '', self.last_name or '')
		else:
			names = ''
		return '%s%s' % (self.username, names)

	def full_name(self):
		return '%s %s %s' % (self.first_name or '', self.last_name or '', self.other_name or '')

	# TODO: Fix these when the backend form for create is valid
	# def clean(self):
	# 	if not (self.account_type and self.is_superuser):
	# 		raise ValidationError({
	# 			'account_type': 'Account type MUST be defined for non superuser.'
	# 		})
	# 	if not (self.status and self.is_superuser):
	# 		raise ValidationError({
	# 			'status': 'Status MUST be defined for non superuser.'
	# 		})
	# 	super(User, self).clean()
	#
	# def save(self, *args, **kwargs):
	# 	if not (self.account_type and self.is_superuser):
	# 		raise ValidationError({
	# 			'account_type': 'Account type MUST be defined for non superuser.'
	# 		})
	# 	if not (self.status and self.is_superuser):
	# 		raise ValidationError({
	# 			'status': 'Status MUST be defined for non superuser.'
	# 		})
	# 	super(User, self).save(*args, **kwargs)
