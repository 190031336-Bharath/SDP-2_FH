# Generated by Django 3.2.2 on 2021-05-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fah', '0002_remove_items_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='food_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Items',
        ),
    ]
