# Generated by Django 4.0.1 on 2022-01-26 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image2',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]