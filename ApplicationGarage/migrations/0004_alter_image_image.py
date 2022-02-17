# Generated by Django 3.2.9 on 2022-02-17 11:06

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('ApplicationGarage', '0003_alllisting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['center'], force_format=None, keep_meta=True, quality=50, size=[300, 300], upload_to='formImages'),
        ),
    ]