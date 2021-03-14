from django.shortcuts import render
from .models import Rota

from rent.models import Category
from sell.models import SellCategory


# Create your views here.



def rotas(request):
    categorys = Category.objects.all()
    sellCategorys = SellCategory.objects.all()
    rota = Rota.objects.all()


    context = {
        'rota':rota,
        'categorys':categorys,
        'sellCategorys':sellCategorys
    }
    return render(request,'tour/rota_list.html',context)