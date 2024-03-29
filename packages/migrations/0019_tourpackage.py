# Generated by Django 4.2.6 on 2024-01-06 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0018_delete_packageset_delete_set1_delete_set2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tourpackage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('packagecategory', models.CharField(choices=[('1daypackage', '1daypackage'), ('2daypackage', '2daypackage'), ('3daypackage', '3daypackage'), ('4daypackage', '4daypackage'), ('5daypackage', '5daypackage'), ('6daypackage', '6daypackage'), ('7daypackage', '7daypackage')], max_length=20)),
                ('district', models.CharField(max_length=100)),
                ('packagenumber', models.PositiveIntegerField()),
                ('daynumber', models.PositiveIntegerField()),
                ('spottime', models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], max_length=20)),
                ('spotname', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='packages.destination')),
            ],
            options={
                'db_table_comment': 'packages for 7day tour selection',
                'ordering': ['id'],
            },
        ),
    ]
