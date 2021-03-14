from django.contrib import admin

from .models import SpecialCategory,SpecialProducts


class SpecialCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':('name',)}

class SpecialProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(SpecialCategory,SpecialCategoryAdmin)
admin.site.register(SpecialProducts, SpecialProductAdmin)
