# Generated by Django 5.1.7 on 2025-03-19 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_blogpage_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='author',
            name='view_name',
            field=models.CharField(default='floran', max_length=255),
            preserve_default=False,
        ),
    ]
