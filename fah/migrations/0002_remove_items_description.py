# Generated by Django 3.2.2 on 2021-05-07 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fah', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='description',
        ),
    ]
