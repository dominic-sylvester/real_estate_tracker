# Generated by Django 2.2.4 on 2020-05-14 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='repair_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='repair_status',
            field=models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], default=1, max_length=3),
        ),
    ]