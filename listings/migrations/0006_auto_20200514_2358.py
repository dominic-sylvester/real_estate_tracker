# Generated by Django 2.2.4 on 2020-05-15 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20200514_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='purchase_amt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='sold_amt',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
