# Generated by Django 3.1.6 on 2021-02-07 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_colorspecs_color_specs_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colorspecs',
            name='color_type',
        ),
    ]
