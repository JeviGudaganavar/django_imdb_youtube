# Generated by Django 3.1 on 2020-09-03 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_movie_poster_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Poster_url',
            field=models.URLField(),
        ),
    ]
