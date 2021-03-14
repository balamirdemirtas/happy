from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class SpecialCategory(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=20, db_index=True, unique=True)

    class Meta:
        ordering = ['-id']
        unique_together =('slug','name')


    def __str__(self):
        return self.name


    #def get_absolute_url(self):
    #    return reverse('special:yunan-adalari', args=[self.slug])




class SpecialProducts(models.Model):
    category = models.ForeignKey(SpecialCategory, related_name='Special', on_delete=models.CASCADE)
    imgseo = models.CharField(max_length=200, db_index=True, default='İmage Seo Alt Ekle')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='special_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextUploadingField()
    strong_content = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=200, db_index=True, default='160 Kelime')
    up_title = models.TextField(max_length=500, default="50-60 Kelime")
    key = models.TextField(max_length=550, default="1 Kelime")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ozel-yat-kiralama:destinasyon', args=[self.slug])