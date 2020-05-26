from django.contrib import admin

from base.models import Status, AccountType, Category, Reaction


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
	list_filter = ('date_created',)
	date_hierarchy = 'date_created'
	list_display = ('name', 'date_modified', 'date_created')
	search_fields = ('name',)


@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
	list_filter = ('date_created',)
	date_hierarchy = 'date_created'
	list_display = ('name', 'status', 'date_modified', 'date_created')
	search_fields = ('name', 'status__name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_filter = ('date_created',)
	date_hierarchy = 'date_created'
	list_display = ('name', 'status', 'date_modified', 'date_created')
	search_fields = ('name', 'status__name')

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
	list_filter = ('date_created',)
	date_hierarchy = 'date_created'
	list_display = ('name', 'status', 'date_modified', 'date_created')
	search_fields = ('name', 'status__name')