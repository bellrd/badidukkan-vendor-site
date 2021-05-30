from django.contrib import admin, messages

from api.models import Item, Price, Tag, Category, Merchandise, Billing


class PriceInline(admin.StackedInline):
    model = Price
    extra = 0
    can_delete = True


class TagInline(admin.StackedInline):
    model = Tag
    extra = 0
    can_delete = True


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [PriceInline, TagInline]
    list_display = ['name', 'is_available']
    list_filter = ['is_available']
    search_fields = ['name', 'category']
    autocomplete_fields = ['category']
    list_editable = ['is_available']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs['queryset'] = Category.objects.filter(added_by=request.user)
        return super(ItemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def has_change_permission(self, request, obj=None):
        try:
            m = Merchandise.objects.get(added_by=request.user)
        except Merchandise.DoesNotExist:
            return False
        if Billing.objects.filter(merchandise=m).count == 0:
            return False
        if Billing.objects.filter(merchandise=m, status="UNPAID").count() != 0:
            return False
        else:
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
