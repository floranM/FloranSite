# Generated by Django 5.1.7 on 2025-03-17 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='IsFeatured',
            field=models.BooleanField(default=False),
        ),
    ]
