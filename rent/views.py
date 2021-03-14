from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from sell.models import SellCategory
from blog.models import Post
from rent.models import İndexComment, Product, Contact, Category,Reservation


def index(request):
    categorys = Category.objects.all()
    sellCategorys = SellCategory.objects.all()
    comments = İndexComment.objects.all()
    products = Product.objects.filter(vitrin__icontains='vitrin').order_by('?')
    context = {
        'products': products,
        'comments': comments,
        'categorys':categorys,
        'sellCategorys':sellCategorys,
    }
    return render(request,'central/index.html',context)


def show(request,category_slug = None):
    categorys = Category.objects.all()
    sellCategorys = SellCategory.objects.all()
    products = Product.objects.filter(available=True).order_by('-id')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'central/show.html',{'products':products,'categorys':categorys,
        'sellCategorys':sellCategorys,})



def detail(request,slug):
    blog = Post.objects.all().order_by('?')
    product = get_object_or_404(Product,slug=slug, available=True)
    smilar = Product.objects.all().order_by('?')
    if 'btnSubmit' in request.POST:
        if True:
            item = product.slug
            name = request.POST.get('name')
            email = request.POST.get('email')
            adult = request.POST.get('adult')
            children = request.POST.get('children')
            telephone = request.POST.get('telephone')
            enter_date = request.POST.get('enter_date')
            out_date = request.POST.get('out_date')
            newRezervation = Reservation.objects.create(product=item, name=name, email=email, adult=adult,
                                                        children=children,
                                                        enter_date=enter_date,out_date=out_date, telephone=telephone)
            newRezervation.save()
            subject = 'Costumer Room Reservation Messages'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, "djangomarmaris@gmail.com"]
            contact_message = "Name:%s\nEmail:%s\nAdult:%s\nChildren:%s\nCheck İn:%s\nTelephone:%s" % (
                name,
                email,
                adult,
                children,
                enter_date,
                telephone,
                )
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
            return redirect('/')

    return render(request,'central/detail.html',{'product':product,'smilar':smilar,'blog':blog})

def contact(request):
    if 'btnSubmit' in request.POST:
        if True:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            subject = 'Contact Messages'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, "djangomarmaris@gmail.com"]
            contact_message = "Name:%s\nEmail:%s\nMessage:%s" % (
                name,
                email,
                message,
            )
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
            return redirect('/')
    return render(request,'central/contact.html')