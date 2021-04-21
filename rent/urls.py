from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views




app_name = 'rent'


urlpatterns =[
    path('',views.index,name ='index'),
    path('contact/',views.contact,name='contact'),
    path('<str:category_slug>', views.show, name='product_list_by_show'),
    path('<str:slug>/<int:id>',views.detail,name='product_detail'),
    path('thx/',views.thx,name='thx'),
]


