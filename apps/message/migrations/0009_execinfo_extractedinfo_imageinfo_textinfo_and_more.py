# Generated by Django 4.0.1 on 2022-03-02 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0008_alter_message_textmsg'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExecInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('execFile', models.FileField(upload_to='files/exec')),
                ('containerImage', models.ImageField(upload_to='images/containers')),
            ],
        ),
        migrations.CreateModel(
            name='ExtractedInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extractedText', models.TextField(blank=True, max_length=5000)),
                ('extractedImage', models.ImageField(blank=True, upload_to='images/extractedImages')),
                ('extractedExecFile', models.FileField(blank=True, upload_to='file/extractedExecFiles')),
            ],
        ),
        migrations.CreateModel(
            name='ImageInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageInfo', models.ImageField(upload_to='images/info')),
                ('containerImage', models.ImageField(upload_to='images/containers')),
            ],
        ),
        migrations.CreateModel(
            name='TextInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textInfo', models.TextField(max_length=5000)),
                ('containerImage', models.ImageField(upload_to='images/containers')),
            ],
        ),
        migrations.AlterField(
            model_name='decryptedmessage',
            name='decryptedText',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='encryptedmessage',
            name='encryptedImage',
            field=models.ImageField(upload_to='images/encrypted'),
        ),
    ]
