from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=20, db_index=True, unique=True)

    class Meta:
        ordering = ['-id']
        unique_together =('slug','name')
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('rent:product_list_by_show', args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='Boats', on_delete = models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    clone = models.CharField(max_length=200, db_index=True)
    vitrin = models.CharField(max_length=200, db_index=True,default='Ürün Vitrin is : vitrin yaz')
    imgseo = models.CharField(max_length=200, db_index=True,default='İmage Seo Alt Ekle')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    info = RichTextUploadingField()
    index_info = models.TextField(max_length=89,default='89 Karakter En fazla')
    general_price = models.DecimalField(max_digits=10, decimal_places=0)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    price_june = models.DecimalField(max_digits=10, decimal_places=0)
    price_july = models.DecimalField(max_digits=10, decimal_places=0)
    price_agust = models.DecimalField(max_digits=10, decimal_places=0)
    price_sept = models.DecimalField(max_digits=10, decimal_places=0)
    price_octo = models.DecimalField(max_digits=10, decimal_places=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    meter = models.CharField(max_length=200, db_index=True,default='Gulet Meter')
    person = models.CharField(max_length=200, db_index=True,default='Gulet Person')
    shower = models.CharField(max_length=200, db_index=True,default='Gulet Shower')
    kabin = models.CharField(max_length=200,db_index=True,default='Toplam Kabin Sayısı Giriniz.')
    aircon = models.CharField(max_length=200,db_index=True,default='Var')
    kabin_type = models.CharField(max_length=200, db_index=True,default='Gulet Double')
    description = models.TextField(max_length=200, db_index=True, default='160 Kelime')
    title = models.TextField(max_length=500,default="50-60 Kelime")
    key = models.TextField(max_length=550,default="1 Kelime")


    class Meta:
        ordering = ['-id']
        index_together = (('id', 'slug',))

    def __str__(self):
        return self.name




class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

class Reservation(models.Model):
    product = models.CharField(max_length=200, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    email = models.EmailField(max_length=70, null=True, blank=True)
    adult = models.CharField(max_length=200, db_index=True)
    children = models.CharField( max_length=200, db_index=True)
    telephone = models.CharField(max_length=200, db_index=True)
    enter_date = models.CharField(max_length=200, db_index=True)
    out_date = models.CharField(max_length=200, db_index=True)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return  self.name



class Contact(models.Model):
    name =  models.CharField(max_length=50, db_index=True, default='Name')
    phone = models.CharField(max_length=50, db_index=True, default='Phone')
    email = models.CharField(max_length=50, db_index=True, default='Emil')
    subject = models.CharField(max_length=50, db_index=True, default='subject')
    text = models.CharField(max_length=50, db_index=True, default='Name')

    def __str__(self):
        return self.name



class İndexComment(models.Model):
    name = models.CharField(max_length=50, db_index=True, default='Name')
    city = models.CharField(max_length=50, db_index=True, default='Phone')
    subject = models.CharField(max_length=50, db_index=True, default='subject')
    text = models.TextField(max_length=263,default='Ürün Aaçıklama 263 Ten az 263 çok olmuyacak')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)

    def __str__(self):
        return self.name