# Generated by Django 2.2.4 on 2019-09-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0013_mdmdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='mdmdata',
            name='date',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='mdmdata',
            name='school_name',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
