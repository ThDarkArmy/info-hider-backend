# Generated by Django 4.0.1 on 2022-03-03 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0009_execinfo_extractedinfo_imageinfo_textinfo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HiddenInfoContainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hiddenInfoContainerImage', models.ImageField(upload_to='images/HiddenInfoContainers')),
            ],
        ),
    ]
