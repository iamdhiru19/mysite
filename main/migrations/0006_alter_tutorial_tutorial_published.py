# Generated by Django 4.1 on 2022-08-28 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_tutorial_tutorial_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 11, 38, 25, 756176, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
