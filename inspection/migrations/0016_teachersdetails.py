# Generated by Django 2.2.4 on 2019-09-13 07:37

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0015_mdmdatadetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachersDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.IntegerField(null=True)),
                ('schName', models.CharField(max_length=500, null=True)),
                ('tName', models.CharField(max_length=500, null=True)),
                ('desig', models.CharField(max_length=500, null=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
