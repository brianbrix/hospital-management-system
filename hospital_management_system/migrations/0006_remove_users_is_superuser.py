# Generated by Django 3.0.5 on 2020-05-06 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_management_system', '0005_auto_20200505_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='is_superuser',
        ),
    ]
