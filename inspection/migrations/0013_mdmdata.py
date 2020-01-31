# Generated by Django 2.2.4 on 2019-09-13 05:33

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0012_remove_schoolselfies_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MDMData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agencyName', models.CharField(max_length=500, null=True)),
                ('numMem', models.CharField(max_length=500, null=True)),
                ('presName', models.CharField(max_length=500, null=True)),
                ('secName', models.CharField(max_length=500, null=True)),
                ('remark', models.CharField(max_length=2000, null=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]