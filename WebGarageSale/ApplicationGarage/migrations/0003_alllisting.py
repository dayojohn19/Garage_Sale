# Generated by Django 3.2.9 on 2022-02-17 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApplicationGarage', '0002_listing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alllisting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listingid', models.IntegerField()),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('link', models.CharField(blank=True, default=None, max_length=64, null=True)),
            ],
        ),
    ]