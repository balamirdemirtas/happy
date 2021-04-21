from django.contrib import admin
from .models import Category,Product,Reservation,Contact,İndexComment,Images




class Gallery(admin.TabularInline):
    model = Images


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':('name',)}



class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','slug','category','price','price_june','price_july','price_agust','price_sept','price_octo','vitrin','available']
    list_editable = ['price','price_june','price_july','price_agust','price_sept','price_octo','available','vitrin']
    prepopulated_fields = {'slug':('name',)}
    inlines = (Gallery,)



admin.site.register(İndexComment)
admin.site.register(Reservation)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Contact)

admin.site.site_header = 'Developer / İhsan Gürol Demirtaş'