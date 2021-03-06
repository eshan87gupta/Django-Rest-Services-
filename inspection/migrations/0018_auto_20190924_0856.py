# Generated by Django 2.2.4 on 2019-09-24 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0017_remove_mdmdata_remark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolselfies',
            old_name='sch_selfie',
            new_name='image',
        ),
        migrations.AddField(
            model_name='schoolselfies',
            name='schName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterModelTable(
            name='hrteachers',
            table='"education_sch"."inspection_hrteachers"',
        ),
        migrations.AlterModelTable(
            name='infrastructuredetails',
            table='"education_sch"."inspection_infrastructuredetails"',
        ),
        migrations.AlterModelTable(
            name='mdmdata',
            table='"education_sch"."inspection_mdmdata"',
        ),
        migrations.AlterModelTable(
            name='mdmdatadetails',
            table='"education_sch"."inspection_mdmdatadetails"',
        ),
        migrations.AlterModelTable(
            name='middaymealquality',
            table='"education_sch"."inspection_middaymealquality"',
        ),
        migrations.AlterModelTable(
            name='schoolmaster',
            table='"education_sch"."inspection_schoolmaster"',
        ),
        migrations.AlterModelTable(
            name='schoolselfies',
            table='"education_sch"."inspection_schoolselfies"',
        ),
        migrations.AlterModelTable(
            name='students',
            table='"education_sch"."inspection_students"',
        ),
        migrations.AlterModelTable(
            name='surveyor_registration',
            table='"education_sch"."inspection_surveyor_registration"',
        ),
        migrations.AlterModelTable(
            name='teachersdetails',
            table='"education_sch"."inspection_teachersdetails"',
        ),
        migrations.AlterModelTable(
            name='teachingquality',
            table='"education_sch"."inspection_teachingquality"',
        ),
    ]
