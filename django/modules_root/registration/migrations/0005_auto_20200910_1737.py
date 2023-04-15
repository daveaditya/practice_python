# Generated by Django 3.1 on 2020-09-10 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20200910_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailverification',
            old_name='nounce',
            new_name='code',
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 10, 18, 37, 19, 422142)),
        ),
        migrations.AlterField(
            model_name='mobileverification',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 10, 17, 42, 18, 422782)),
        ),
    ]
