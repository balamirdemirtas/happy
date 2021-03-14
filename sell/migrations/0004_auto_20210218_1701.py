# Generated by Django 3.0.5 on 2021-02-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0003_auto_20210218_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellproduct',
            name='beam',
            field=models.CharField(db_index=True, default='Example', max_length=200),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='draft',
            field=models.CharField(db_index=True, default='Example', max_length=200),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='engineHours',
            field=models.CharField(db_index=True, default='Example', max_length=200),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='noOfEngines',
            field=models.CharField(db_index=True, default='Example', max_length=200),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='noOfPreviousOwner',
            field=models.CharField(db_index=True, default='Example', max_length=200),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='rudder',
            field=models.CharField(db_index=True, default='Example', max_length=200),
        ),
    ]
