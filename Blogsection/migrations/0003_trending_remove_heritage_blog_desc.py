# Generated by Django 4.2.6 on 2023-11-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogsection', '0002_heritage'),
    ]

    operations = [
        migrations.CreateModel(
            name='trending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_img', models.FileField(max_length=250, null=None, upload_to='blog-img/')),
                ('blog_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='heritage',
            name='blog_desc',
        ),
    ]
