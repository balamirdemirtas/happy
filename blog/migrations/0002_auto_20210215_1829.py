# Generated by Django 3.0.5 on 2021-02-15 18:29

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='smiler',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='strong_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
