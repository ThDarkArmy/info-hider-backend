# Generated by Django 4.0.1 on 2022-02-05 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='textMsg',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
