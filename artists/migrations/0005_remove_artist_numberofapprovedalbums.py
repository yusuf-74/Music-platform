# Generated by Django 4.1.3 on 2022-11-06 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0004_artist_numberofapprovedalbums'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='numberOfApprovedAlbums',
        ),
    ]