from django.contrib import admin

from api.models import (Owner, OwnerDocument, Merchandise)


class OwnerDocumentInline(admin.StackedInline):
    model = OwnerDocument
    extra = 0
    can_delete = False


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    inlines = [OwnerDocumentInline]
    list_display = ['name', 'mobile_number', 'email', 'bank_account', 'ifsc_code']
    search_fields = ['name', 'mobile_number']

    exclude = ['added_by']

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return []
        else:
            return ['added_by']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'added_by', None) is None:
            obj.added_by = request.user
        obj.save()

    # def has_view_permission(self, request, obj=None):
    #     return False

    def has_add_permission(self, request):
        return Owner.objects.filter(added_by=request.user).count() == 0
