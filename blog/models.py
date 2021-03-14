from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    imgseo = models.CharField(max_length=200, db_index=True, default='İmage Seo Alt Ekle')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200, db_index=True, default='Wogo Yachting')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    description = models.TextField(max_length=200, db_index=True, default='160 Kelime')
    up_title = models.TextField(max_length=500, default="50-60 Kelime")
    key = models.TextField(max_length=550, default="1 Kelime")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])

