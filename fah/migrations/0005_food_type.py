# Generated by Django 3.2.2 on 2021-05-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fah', '0004_auto_20210507_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Starters', 'Starters'), ('Main course', 'Main Course'), ('Desert', 'Desert'), ('Snacks', 'Snacks'), ('Drinks', 'Drinks')], max_length=50)),
            ],
        ),
    ]
