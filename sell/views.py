from django.shortcuts import render, get_object_or_404,redirect
from rent.models import Category
from django.conf import settings
from django.core.mail import send_mail
from blog.models import Post
from .models import SellCategory, SellProduct, SalesShip


# Create your views here.

def sell_list(request):
    categorys = Category.objects.all()
    sellCategorys = SellCategory.objects.all()
    products = SellProduct.objects.filter(vitrin__icontains='vitrin').order_by('?')
    context = {
        'products': products,
        'categorys':categorys,
        'sellCategorys':sellCategorys
    }
    return render(request,'ship/sell_list.html',context)



def show(request,category_slug = None):
    categorys = Category.objects.all()
    sellCategorys = SellCategory.objects.all()
    products = SellProduct.objects.filter(available=True).order_by('-id')
    if category_slug:
        category = get_object_or_404(SellCategory, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'ship/sell_list.html',{'products':products,'categorys':categorys,'sellCategorys':sellCategorys})



def detail(request,slug):
    categorys = Category.objects.all()
    sellCategorys = SellCategory.objects.all()
    blog = Post.objects.all().order_by('?')
    product = get_object_or_404(SellProduct,slug=slug, available=True)
    smilar = SellProduct.objects.all().order_by('?')
    if 'btnSubmit' in request.POST:
        if True:
            item = product.slug
            name = request.POST.get('name')
            email = request.POST.get('email')
            text = request.POST.get('text')
            newRezervation = SalesShip.objects.create(product=item,name=name,email=email,text=text)
            newRezervation.save()
            subject = 'Costumer Room Reservation Messages'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, "djangomarmaris@gmail.com"]
            contact_message = "Name : %s\nEmail : %s\nText : %s" % (
                name,
                email,
               text,
                )
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
            return redirect('/')
    return render(request,'ship/sell_detail.html',{'product':product,'smilar':smilar,'blog':blog,'categorys':categorys,'sellCategorys':sellCategorys})