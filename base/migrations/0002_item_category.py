# Generated by Django 4.1.4 on 2023-01-13 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='base.category'),
        ),
    ]
