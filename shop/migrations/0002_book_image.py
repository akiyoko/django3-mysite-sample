# Generated by Django 3.2.3 on 2021-06-01 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='画像'),
        ),
    ]
