# Generated by Django 3.0.5 on 2021-02-21 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rota', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rota',
            old_name='exit',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='rota',
            name='slug',
        ),
    ]