# Generated by Django 3.2.2 on 2021-05-07 18:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fah', '0003_auto_20210507_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_items',
            name='image',
            field=models.ImageField(default=1, upload_to='products/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food_items',
            name='type',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Starters', 'Starters'), ('Main course', 'Main Course'), ('Desert', 'Desert'), ('Snacks', 'Snacks'), ('Drinks', 'Drinks')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
