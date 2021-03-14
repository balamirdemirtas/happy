# Generated by Django 3.0.5 on 2021-02-16 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exit', models.CharField(max_length=200, unique=True)),
                ('rota', models.CharField(default='Bölge', max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('imgseo', models.CharField(db_index=True, default='İmage Seo Alt Ekle', max_length=200)),
                ('liman', models.TextField(default='Açılama Giriniz.')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(db_index=True, default='160 Kelime', max_length=200)),
                ('up_title', models.TextField(default='50-60 Kelime', max_length=500)),
                ('key', models.TextField(default='1 Kelime', max_length=550)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
