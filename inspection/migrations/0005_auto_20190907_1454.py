# Generated by Django 2.2.4 on 2019-09-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0004_auto_20190905_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolmaster',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='schoolmaster',
            name='lon',
            field=models.FloatField(null=True),
        ),
    ]
