# Generated by Django 3.0.5 on 2021-03-13 17:56

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0007_salesship_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellcategory',
            name='name_de',
            field=models.CharField(db_index=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='sellcategory',
            name='name_en',
            field=models.CharField(db_index=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='sellcategory',
            name='name_ru',
            field=models.CharField(db_index=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='sellcategory',
            name='name_tr',
            field=models.CharField(db_index=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='aircon_de',
            field=models.CharField(db_index=True, default='Var', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='aircon_en',
            field=models.CharField(db_index=True, default='Var', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='aircon_ru',
            field=models.CharField(db_index=True, default='Var', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='aircon_tr',
            field=models.CharField(db_index=True, default='Var', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='boatHull_de',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='boatHull_en',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='boatHull_ru',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='boatHull_tr',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='flag_de',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='flag_en',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='flag_ru',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='flag_tr',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='index_info_de',
            field=models.TextField(default='89 Karakter En fazla', max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='index_info_en',
            field=models.TextField(default='89 Karakter En fazla', max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='index_info_ru',
            field=models.TextField(default='89 Karakter En fazla', max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='index_info_tr',
            field=models.TextField(default='89 Karakter En fazla', max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='info_de',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='info_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='info_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='info_tr',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='kabin_de',
            field=models.CharField(db_index=True, default='Toplam Kabin Sayısı Giriniz.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='kabin_en',
            field=models.CharField(db_index=True, default='Toplam Kabin Sayısı Giriniz.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='kabin_ru',
            field=models.CharField(db_index=True, default='Toplam Kabin Sayısı Giriniz.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='kabin_tr',
            field=models.CharField(db_index=True, default='Toplam Kabin Sayısı Giriniz.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='kabin_type_de',
            field=models.CharField(db_index=True, default='Gulet Double', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='kabin_type_en',
            field=models.CharField(db_index=True, default='Gulet Double', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='kabin_type_ru',
            field=models.CharField(db_index=True, default='Gulet Double', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='kabin_type_tr',
            field=models.CharField(db_index=True, default='Gulet Double', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='name_de',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='name_en',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='name_ru',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='name_tr',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='producer_de',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='producer_en',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='producer_ru',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='producer_tr',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='rudder_de',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='rudder_en',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='rudder_ru',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='rudder_tr',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='saleType_de',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='saleType_en',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='saleType_ru',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='saleType_tr',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='sale_de',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='sale_en',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='sale_ru',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='sale_tr',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='status_de',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='status_en',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='status_ru',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='status_tr',
            field=models.CharField(db_index=True, default='Example', max_length=200, null=True),
        ),
    ]
