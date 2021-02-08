# Generated by Django 3.1.6 on 2021-02-07 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_colorspecs_color_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='colorspecs',
            name='color_type',
            field=models.CharField(choices=[('RGB', 'RGB'), ('HSL', 'HSL'), ('BRGB', 'BRGB')], default='RGB', max_length=4),
        ),
    ]
