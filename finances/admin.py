from django.contrib import admin

from .models import BaseFinance, Debt, OuterwearDetail, Product, Size, Category, OtherDetail, SendTo

admin.site.register(BaseFinance)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(OtherDetail)


class SendToAdmin(admin.ModelAdmin):
    fields = ('fcs', 'where')


class OuterWearInline(admin.TabularInline):
    model = OuterwearDetail
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        OuterWearInline,
    ]
    list_display = ['name', 'available', 'quantity']


class DebtAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'value']


admin.site.register(Product, ProductAdmin)
admin.site.register(Debt, DebtAdmin)
admin.site.register(SendTo, SendToAdmin)

