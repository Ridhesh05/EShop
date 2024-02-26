from django.contrib import admin
from .models import Products
from .models import Order
admin.site.site_header = 'Ecommerce-Site'

admin.site.index_title = 'Manage EShop'

admin.site.site_title="EShop"




# List out all field which you want to display 

class ProductAdmin(admin.ModelAdmin):
    # create an object to change category  name in list view
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    list_display=('title','price','discount_price','category','description')
    search_fields=('title','description')
    actions={change_category_to_default,}#always add , at last 
    #to display limited fields of product
    fields=('title','description')
    list_editable=('price',)
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)
