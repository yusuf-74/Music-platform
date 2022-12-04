# Generated by Django 4.1.3 on 2022-12-04 13:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(default='New Album', max_length=150)),
                ('creationDateTime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created on')),
                ('releaseDateTime', models.DateTimeField(default=datetime.datetime.now, verbose_name='released on')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('isApproved', models.BooleanField(default=False, verbose_name='Approved')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='artists.artist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Song', max_length=150)),
                ('image', models.ImageField(upload_to='songs/%y/%m/%d')),
                ('audioFile', models.FileField(upload_to='audio/%y/%m/%d')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='songs', to='albums.album')),
            ],
        ),
    ]
