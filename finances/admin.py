from django.contrib import admin

from .models import BaseFinance, Debt, OuterwearDetail, Product, Size, Category

admin.site.register(BaseFinance)
admin.site.register(Category)
admin.site.register(Size)


# class SizeInline(admin.StackedInline):
# 	model = Size


class OuterWearInline(admin.TabularInline):
	model = OuterwearDetail
	extra = 0


class ProductAdmin(admin.ModelAdmin):
	inlines = [
		OuterWearInline,
	]


admin.site.register(Product, ProductAdmin)
