# Generated by Django 4.1 on 2022-08-23 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=100)),
                ('qr_image', models.ImageField(blank=True, null=True, upload_to='QRCode')),
            ],
            options={
                'verbose_name_plural': 'persons',
            },
        ),
    ]
