from django.contrib import admin
from django.contrib.admin import register

from api.models import User


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile_number','is_root']
    list_filter = ['is_root' ]

    def has_change_permission(self, request, obj=None):
        return request.user.is_root

    def has_add_permission(self, request):
        return request.user.is_root

    def has_delete_permission(self, request, obj=None):
        return request.user.is_root

    def has_module_permission(self, request):
        return request.user.is_root
