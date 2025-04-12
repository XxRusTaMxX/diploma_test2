# Generated by Django 4.0.4 on 2022-05-25 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_movie_flyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='popularity',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdbid',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
