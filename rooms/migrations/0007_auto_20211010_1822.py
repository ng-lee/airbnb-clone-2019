# Generated by Django 2.2.5 on 2021-10-10 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20211010_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='room_photo'),
        ),
    ]
