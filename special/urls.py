from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views




app_name = 'special'


urlpatterns =[
    path('<str:category_slug>/',views.special_list,name='category'),
    path('destination/<str:slug>/',views.special_detail,name='destinasyon'),
]


