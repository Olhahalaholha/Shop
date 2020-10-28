from django.contrib import admin
from . models import Products, Order
# Register your models here.



# change admin panel
admin.site.site_header  = "E-com site"
admin.site.site_title = "Shopping"
admin.site.index_title = "Manage ABC Schopping"


# change admin panel
class ProductAdmin(admin.ModelAdmin):

	def change_category_to_default(self, request, queryset):
		queryset.update(category="default")
		queryset.update(category="fashion")


	change_category_to_default.short_description = "Default category"
	list_display = ('title', 'price', 'discount_price', 'category', 'description',)
	search_fields  = ('title',)
	
	# меняем функцией change_category_to_default  категорию на нужную
	actions = ('change_category_to_default',)

	# какие поля всвечиваются если кликнеш на один из продуктов 
	fields = ('title', 'price',)

	# every iem can change in panel Products (do not neet open every product)
	list_editable = ('price', 'category',)


admin.site.register(Products, ProductAdmin)
admin.site.register(Order)
