from django.contrib import admin

# Register your models here.

from catalog.models import AccountInfo

# admin.site.register(AccountInfo)

# Define the admin class


class AccountInfoAdmin(admin.ModelAdmin):
    list_display = ('django_user', 'name', 'type')

# Register the admin class with the associated model
admin.site.register(AccountInfo, AccountInfoAdmin)