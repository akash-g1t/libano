from django.contrib import admin
from .models import Banking, Address

from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Banking)
class BankingAdmin(admin.ModelAdmin):
    list_display = ['email', 'url', 'account_number', 'ifsc_code', 'expiry_date', 'approve_status', 'created_at', 'amount']
    search_fields = ['email', 'account_number']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['url', 'created_at', 'updated_at']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False