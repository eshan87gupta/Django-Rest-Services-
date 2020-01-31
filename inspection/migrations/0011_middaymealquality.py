# Generated by Django 2.2.4 on 2019-09-09 14:30

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0010_teachingquality'),
    ]

    operations = [
        migrations.CreateModel(
            name='MidDayMealQuality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=500, null=True)),
                ('date', models.CharField(max_length=500, null=True)),
                ('kit_shed', models.CharField(max_length=500, null=True)),
                ('cond_kit_shed', models.CharField(max_length=500, null=True)),
                ('loc', models.CharField(max_length=500, null=True)),
                ('menu', models.CharField(max_length=500, null=True)),
                ('fuel', models.CharField(max_length=500, null=True)),
                ('shed_paint', models.CharField(max_length=500, null=True)),
                ('enough_utensil', models.CharField(max_length=500, null=True)),
                ('agency', models.CharField(max_length=500, null=True)),
                ('clean_cooks', models.CharField(max_length=500, null=True)),
                ('ingred', models.CharField(max_length=500, null=True)),
                ('tasted', models.CharField(max_length=500, null=True)),
                ('teacher_tasted', models.CharField(max_length=500, null=True)),
                ('acc_menu', models.CharField(max_length=500, null=True)),
                ('food_sealed', models.CharField(max_length=500, null=True)),
                ('hand_wash', models.CharField(max_length=500, null=True)),
                ('mothers_checked', models.CharField(max_length=500, null=True)),
                ('panji', models.CharField(max_length=500, null=True)),
                ('payment', models.CharField(max_length=500, null=True)),
                ('food_right_price', models.CharField(max_length=500, null=True)),
                ('food_stored', models.CharField(max_length=500, null=True)),
                ('stored_food_good', models.CharField(max_length=500, null=True)),
                ('teach_manage_part', models.CharField(max_length=500, null=True)),
                ('milk_distributed', models.CharField(max_length=500, null=True)),
                ('milk_powder', models.CharField(max_length=500, null=True)),
                ('complaint', models.CharField(max_length=500, null=True)),
                ('vit_tabs', models.CharField(max_length=500, null=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
