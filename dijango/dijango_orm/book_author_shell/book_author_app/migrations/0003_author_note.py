# Generated by Django 3.2.3 on 2021-05-26 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_author_app', '0002_alter_book_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='note',
            field=models.TextField(default='no comments'),
        ),
    ]
