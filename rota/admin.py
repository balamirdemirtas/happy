from django.contrib import admin

from .models import Rota





class RotaAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')



admin.site.register(Rota, RotaAdmin)

