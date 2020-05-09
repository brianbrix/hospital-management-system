# Generated by Django 3.0.5 on 2020-05-06 22:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_management_system', '0007_auto_20200506_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors',
            name='is_superuser',
        ),
        migrations.AlterField(
            model_name='doctors',
            name='creationdate',
            field=models.DateTimeField(blank=True, db_column='creationDate', default=datetime.datetime(2020, 5, 6, 22, 39, 16, 95701), null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='regdate',
            field=models.DateTimeField(blank=True, db_column='regDate', default=datetime.datetime(2020, 5, 6, 22, 39, 16, 94446), null=True),
        ),
    ]