# Generated by Django 2.1.2 on 2018-11-07 06:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.AddField(
            model_name='article',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=None, null=True, size=None),
        ),
    ]