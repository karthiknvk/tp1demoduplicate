# Generated by Django 4.2.6 on 2023-12-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0015_rename_packagnumber_twodaypackage_packagenumber_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onedaypackage',
            old_name='packagnumber',
            new_name='packagenumber',
        ),
        migrations.RenameField(
            model_name='onedaypackage',
            old_name='spotnumber',
            new_name='spottime',
        ),
        migrations.AddField(
            model_name='onedaypackage',
            name='daynumber',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
