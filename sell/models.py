from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class SellCategory(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=20, db_index=True, unique=True)

    class Meta:
        ordering = ['-id']
        unique_together = ('slug', 'name')
        verbose_name_plural = 'Sell Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sale:sale_list_by_show', args=[self.slug])


class SellProduct(models.Model):
    category = models.ForeignKey(SellCategory, related_name='Boats', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    clone = models.CharField(max_length=200, db_index=True,default='Example')
    vitrin = models.CharField(max_length=200, db_index=True, default='Ürün Vitrin is : vitrin yaz')
    imgseo = models.CharField(max_length=200, db_index=True, default='İmage Seo Alt Ekle')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image4 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image5 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image6 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image7 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image8 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image9 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image10 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image11 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image12 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image13 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image14 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image15 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    info = RichTextUploadingField()
    index_info = models.TextField(max_length=89, default='89 Karakter En fazla')
    general_price = models.DecimalField(max_digits=10, decimal_places=0)
    meter = models.CharField(max_length=200, db_index=True, default='Gulet Meter')
    person = models.CharField(max_length=200, db_index=True, default='Gulet Person')
    shower = models.CharField(max_length=200, db_index=True, default='Gulet Shower')
    kabin = models.CharField(max_length=200, db_index=True, default='Toplam Kabin Sayısı Giriniz.')
    aircon = models.CharField(max_length=200, db_index=True, default='Var')
    kabin_type = models.CharField(max_length=200, db_index=True, default='Gulet Double')
    available = models.BooleanField(default=True)
    producer = models.CharField(max_length=200, db_index=True,default='Example')
    model = models.CharField(max_length=200, db_index=True,default='Example')
    year = models.CharField(max_length=200, db_index=True,default='Example')
    flag = models.CharField(max_length=200, db_index=True,default='Example')
    beam = models.CharField(max_length=200, db_index=True, default='Example')
    draft = models.CharField(max_length=200, db_index=True, default='Example')
    length = models.CharField(max_length=200, db_index=True,default='Example')
    weight = models.CharField(max_length=200, db_index=True,default='Example')
    certificate = models.CharField(max_length=200, db_index=True,default='Example')
    firstLaunch = models.CharField(max_length=200, db_index=True,default='Example')
    noOfPreviousOwner = models.CharField(max_length=200, db_index=True,default='Example')
    status = models.CharField(max_length=200, db_index=True,default='Example')
    saleType = models.CharField(max_length=200, db_index=True,default='Example')
    sale = models.CharField(max_length=200, db_index=True,default='Example')
    rudder = models.CharField(max_length=200, db_index=True,default='Example')
    motorCompany = models.CharField(max_length=200, db_index=True,default='Example')
    noOfEngines = models.CharField(max_length=200, db_index=True,default='Example')
    engineHours = models.CharField(max_length=200, db_index=True,default='Example')
    hp = models.CharField(max_length=200, db_index=True,default='Example')
    fuel = models.CharField(max_length=200, db_index=True,default='Example')
    boatHull = models.CharField(max_length=200, db_index=True,default='Example')
    fuelCapacity = models.CharField(max_length=200, db_index=True,default='Example')
    waterCapacity = models.CharField(max_length=200, db_index=True,default='Example')
    metarialDeck = models.CharField(max_length=200, db_index=True,default='Example')
    cabin = models.CharField(max_length=200, db_index=True,default='Example')
    wc = models.CharField(max_length=200, db_index=True,default='Example')
    headroom =  models.CharField(max_length=200, db_index=True,default='Example')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=200, db_index=True, default='160 Kelime')
    title = models.TextField(max_length=500, default="50-60 Kelime")
    key = models.TextField(max_length=550, default="1 Kelime")

    class Meta:
        ordering = ['-id']
        index_together = (('id', 'slug',))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sale:sale_detail', args=[self.slug])



class SalesShip(models.Model):
    product = models.CharField(max_length=200, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    email= models.CharField(max_length=200, db_index=True)
    telephone = models.CharField(max_length=200, db_index=True)
    text = models.TextField(max_length=200, db_index=True, default='160 Kelime')


    def __str__(self):
        return self.name

