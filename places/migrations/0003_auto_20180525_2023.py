# Generated by Django 2.1a1 on 2018-05-25 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20180524_1836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
    ]