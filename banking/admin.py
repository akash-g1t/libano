from django.contrib import admin
from .models import Banking

from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Banking)
class BankingAdmin(admin.ModelAdmin):
    list_display = ['email', 'url', 'account_number', 'ifsc_code', 'expiry_date', 'approve_status', 'created_at', 'amount']
    search_fields = ['email', 'account_number']
