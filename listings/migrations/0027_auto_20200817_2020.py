# Generated by Django 2.2.4 on 2020-08-18 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0026_auto_20200817_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documents',
            old_name='document',
            new_name='document2',
        ),
        migrations.AddField(
            model_name='documents',
            name='document1',
            field=models.FileField(default=1, upload_to='documents/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documents',
            name='document3',
            field=models.FileField(blank=True, upload_to='documents/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='documents',
            name='document4',
            field=models.FileField(blank=True, upload_to='documents/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='documents',
            name='document5',
            field=models.FileField(blank=True, upload_to='documents/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='documents',
            name='title',
            field=models.CharField(default='title', max_length=200),
        ),
    ]