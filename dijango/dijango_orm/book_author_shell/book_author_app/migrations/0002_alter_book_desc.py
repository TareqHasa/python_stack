# Generated by Django 3.2.3 on 2021-05-26 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_author_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.TextField(default='no description'),
        ),
    ]
