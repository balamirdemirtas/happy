from django.shortcuts import render,get_object_or_404
from .models import Post
from rent.models import Product
from django.core.paginator import Paginator
from rent.models import Category
from sell.models import SellCategory
# Create your views here.


def blog(request):
    categorys = Category.objects.all()
    sellCategorys = SellCategory.objects.all()
    ship = Product.objects.all().order_by('?')
    posts = Post.objects.all().order_by('id')

    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request,'history/blog_list.html',{'posts':posts,'ship':ship,'categorys':categorys,'sellCategorys':sellCategorys})

def blog_detail(request,slug):
    categorys = Category.objects.all()
    sellCategorys = SellCategory.objects.all()
    ship = Product.objects.filter(clone__icontains='gulet').order_by('?')[0:12]
    blog = Post.objects.all().order_by('?')
    product = get_object_or_404(Post, slug=slug)
    return render(request,'history/blog_detail.html',{'product':product,'ship':ship,'blog':blog,'categorys':categorys,'sellCategorys':sellCategorys})