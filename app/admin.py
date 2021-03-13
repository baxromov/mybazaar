from django.contrib import admin
from . import models
from mptt import admin as mptt_admin


class AddressAdmin(admin.StackedInline):
    model = models.Address


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = (AddressAdmin, )
    exclude = (
        'user_permissions',
        'is_superuser',
        'date_joined',
        'is_active',
        'is_staff',
        'groups',
    )
    readonly_fields = [
        'last_login',
    ]


@admin.register(models.Category)
class CategoryAdmin(mptt_admin.DraggableMPTTAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    pass
