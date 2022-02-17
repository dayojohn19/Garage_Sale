# Generated by Django 3.2.9 on 2022-02-17 01:38

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApplicationGarage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=64)),
                ('link', models.ImageField(blank=True, default=None, max_length=64, null=True, storage=django.core.files.storage.FileSystemStorage(location='/formImages'), upload_to='')),
                ('time', models.CharField(max_length=64)),
            ],
        ),
    ]