# Generated by Django 3.2.2 on 2021-05-11 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fah', '0006_alter_food_items_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_items',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fah.food_type'),
        ),
    ]
