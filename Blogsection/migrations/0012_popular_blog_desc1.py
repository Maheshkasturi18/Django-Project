# Generated by Django 4.2.6 on 2023-11-30 07:50

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogsection', '0011_latest_blog_desc_latest_blog_title2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='popular',
            name='blog_desc1',
            field=tinymce.models.HTMLField(default=404),
            preserve_default=False,
        ),
    ]
