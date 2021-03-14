from django.contrib import admin
from .models import SellCategory,SellProduct,SalesShip



class SellCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':('name',)}



class SellProductAdmin(admin.ModelAdmin):
    list_display = ['id','slug','category','general_price','vitrin','available']
    list_editable = ['general_price','available','vitrin']
    prepopulated_fields = {'slug':('name',)}



class SalesShipAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(SellCategory,SellCategoryAdmin)
admin.site.register(SellProduct,SellProductAdmin)
admin.site.register(SalesShip,SalesShipAdmin)
admin.site.site_header = 'Groundwork From By Wogo Yachting - Developer / İhsan Gürol Demirtaş'