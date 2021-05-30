from django.contrib import admin
from django.contrib.admin import register

from api.models import Billing


@register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ['merchandise', 'amount', 'status', 'payment_link']
    list_filter = ['merchandise', 'status']

    def has_change_permission(self, request, obj=None):
        return request.user.is_root

    def has_add_permission(self, request):
        return request.user.is_root

    def has_delete_permission(self, request, obj=None):
        return request.user.is_root

    def has_module_permission(self, request):
        return request.user.is_root
