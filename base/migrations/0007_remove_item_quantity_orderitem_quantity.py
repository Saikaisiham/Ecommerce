# Generated by Django 4.1.4 on 2023-01-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_discription_item_description_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
