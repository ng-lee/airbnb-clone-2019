# Generated by Django 2.2.5 on 2021-10-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20211010_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('comfirmed', 'Confirmed'), ('canceled', 'Canceled')], max_length=10),
        ),
    ]
