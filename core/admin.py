"""
Core admin setup
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.forms import CustomUserCreationForm
from core.models import User, Post


@admin.register(User)
class UserCoreAdmin(UserAdmin):
	fieldsets = (
		(_('Credentials'), {'fields': ('username', 'password')}),
		(_('Personal info'), {
			'fields': ('first_name', 'last_name', 'other_name', 'email', 'phone_number', 'gender')}),
		(_('Others'), {'fields': ('bio', 'profile_image_url', 'account_type', 'status')}),
		(_('Permissions'), {
			'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
		}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'account_type', 'status', 'password1', 'password2'),
		}),
	)

	add_form = CustomUserCreationForm

	list_filter = ('date_created', 'gender', 'account_type', 'status')
	date_hierarchy = 'date_created'
	list_display = (
		'username', 'full_name', 'gender', 'email', 'phone_number', 'account_type', 'status', 'date_modified',
		'date_created')
	search_fields = (
		'username', 'full_name', 'gender', 'email', 'phone_number', 'account_type__name', 'status__name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	"""
	Admin model for Post entity.
	"""
	list_filter = ('date_created', 'category', 'featured')
	date_hierarchy = 'date_created'
	list_display = (
		'title', 'excerpt', 'user', 'featured', 'category', 'priority', 'comments_count', 'reactions_count', 'status',
		'date_modified', 'date_created')
	search_fields = (
		'title', 'content', 'user__first_name', 'user__last_name', 'user__other_name', 'category__name',
		'priority', 'comments_count', 'reactions_count', 'status__name')
