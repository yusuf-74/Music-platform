# Generated by Django 4.1.3 on 2022-11-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_album_isapproved_alter_album_artist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='isApproved',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
    ]