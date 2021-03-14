from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404

from sell.models import SellCategory
from .models import SpecialProducts,SpecialCategory

from rent.models import Product,Category
# Create your views here.




def special_list(request, category_slug = None):
    categorys = Category.objects.all()
    sellCategorys = SellCategory.objects.all()
    ship = Product.objects.filter(clone__icontains='gulet').order_by('?')
    products = SpecialProducts.objects.all().order_by('-id')

    if category_slug:
        category = get_object_or_404(SpecialCategory, slug=category_slug)
        products = products.filter(category=category)

        paginator = Paginator(products, 8)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)
    return render(request,'medium/special_list.html',{'category':category,'products':products,'ship':ship,'categorys':categorys,'sellCategorys':sellCategorys})



def special_detail(request,slug):
    categorys = Category.objects.all()
    sellCategorys = SellCategory.objects.all()
    ship = Product.objects.filter(clone__icontains='gulet').order_by('?')
    product = get_object_or_404(SpecialProducts,slug=slug)
    return render(request,'medium/special_detail.html',{'product':product,'ship':ship,'categorys':categorys,'sellCategorys':sellCategorys})
