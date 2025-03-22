# Generated by Django 5.1.7 on 2025-03-21 22:43

import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_blogpage_tags_delete_blogpagetag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.tag'),
        ),
    ]
