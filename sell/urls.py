from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views




app_name = 'sell'


urlpatterns =[
    path('list/',views.sell_list,name ='index'),
    path('<str:category_slug>', views.show, name='sale_list_by_show'),
    path('ship/<str:slug>/',views.detail,name='sale_detail'),
]


