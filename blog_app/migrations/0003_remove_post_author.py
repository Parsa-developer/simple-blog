# Generated by Django 5.2.1 on 2025-05-09 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
