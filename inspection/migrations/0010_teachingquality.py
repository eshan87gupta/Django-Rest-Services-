# Generated by Django 2.2.4 on 2019-09-09 11:48

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0009_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachingQuality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=500, null=True)),
                ('date', models.CharField(max_length=500, null=True)),
                ('standard', models.CharField(max_length=500, null=True)),
                ('syll_status', models.CharField(max_length=500, null=True)),
                ('lang_level', models.CharField(max_length=500, null=True)),
                ('math_level', models.CharField(max_length=500, null=True)),
                ('gen_level', models.CharField(max_length=500, null=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]