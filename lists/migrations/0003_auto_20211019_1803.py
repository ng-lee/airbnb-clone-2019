# Generated by Django 2.2.5 on 2021-10-19 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20211010_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='room',
            new_name='rooms',
        ),
    ]
