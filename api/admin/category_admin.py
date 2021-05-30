from django.contrib import admin
from django.contrib import messages
from django.contrib.admin import register

from api.models import Category, Merchandise, Billing


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['merchandise', 'added_by']
    search_fields = ['name']
    list_display = ['name', 'merchandise', 'is_available']

    def get_queryset(self, request):
        return Category.objects.filter(added_by=request.user)

    def save_model(self, request, obj, form, change):
        try:
            obj.merchandise = Merchandise.objects.get(added_by=request.user)
        except Merchandise.DoesNotExist:
            messages.add_message(request, messages.ERROR, "Create Merchandise first")
            return
        obj.added_by = request.user
        obj.save()

    def has_change_permission(self, request, obj=None):
        try:
            m = Merchandise.objects.get(added_by=request.user)
        except Merchandise.DoesNotExist:
            return False

        if Billing.objects.filter(merchandise=m).count() == 0:
            return False
        if Billing.objects.filter(merchandise=m, status="UNPAID").count() != 0:
            return False
        else:
            return True

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        try:
            m = Merchandise.objects.get(added_by=request.user)
            if Billing.objects.filter(merchandise=m).count() == 0:
                return False
            if Billing.objects.filter(merchandise=m, status='UNPAID').count() != 0:
                return False
            else:
                return True
        except Merchandise.DoesNotExist:
            return False
