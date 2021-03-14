from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.db import models









class Rota(models.Model):
    name = models.CharField(max_length=200, unique=True)
    rota = models.CharField(max_length=200,default='Bölge')
    exit = models.CharField(max_length=200,default='exit')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    imgseo = models.CharField(max_length=200, db_index=True, default='İmage Seo Alt Ekle')
    liman = models.TextField(default='Açılama Giriniz.')
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=200, db_index=True, default='160 Kelime')
    up_title = models.TextField(max_length=500, default="50-60 Kelime")
    key = models.TextField(max_length=550, default="1 Kelime")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mavi-yolculuk:rotalar')
