# Generated by Django 4.1.4 on 2022-12-18 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_like_value_post_liked'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]
