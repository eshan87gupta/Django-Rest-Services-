# Generated by Django 2.2.4 on 2019-09-05 07:11

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0002_auto_20190905_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='surveyor_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surveyor_name', models.CharField(max_length=100, null=True)),
                ('surveyor_designation', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=11, null=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
