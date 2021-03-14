from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views




app_name = 'rota'


urlpatterns =[
    path('list/',views.rotas,name='rotas'),
]


