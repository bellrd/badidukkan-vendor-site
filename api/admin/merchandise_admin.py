from django.contrib import admin

from api.models import MerchandiseDocument, Merchandise, Owner, User


class MerchandiseDocumentInline(admin.StackedInline):
    model = MerchandiseDocument
    can_delete = False
    extra = 0


@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    inlines = [MerchandiseDocumentInline]
    list_display = ['name', 'added_by', 'is_available']
    list_editable = ['is_available']

    def get_exclude(self, request, obj=None):
        if request.user.is_root:
            return []
        else:
            return ['state', 'added_by']

    fieldsets = (
        (
            'Details', {'fields': (
                'owner', 'name', 'tag_line', 'photo_url', 'address',)}
        ),
        (
            'Available', {'fields': ('is_available',)}
        ),
    )

    def get_queryset(self, request):
        return Merchandise.objects.filter(added_by=request.user)

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        obj.save()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "owner":
            kwargs['queryset'] = Owner.objects.filter(added_by=request.user)
        elif db_field.name == "vendor":
            kwargs['queryset'] = User.objects.filter(id=request.user.id)
        return super(MerchandiseAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def has_add_permission(self, request):
        return Merchandise.objects.filter(added_by=request.user).count() == 0
