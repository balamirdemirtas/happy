# Generated by Django 3.0.5 on 2021-02-15 19:51

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ['-id'],
                'unique_together': {('slug', 'name')},
            },
        ),
        migrations.CreateModel(
            name='SpecialProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgseo', models.CharField(db_index=True, default='İmage Seo Alt Ekle', max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('list_content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('strong_content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(db_index=True, default='160 Kelime', max_length=200)),
                ('up_title', models.TextField(default='50-60 Kelime', max_length=500)),
                ('key', models.TextField(default='1 Kelime', max_length=550)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Special', to='special.SpecialCategory')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
