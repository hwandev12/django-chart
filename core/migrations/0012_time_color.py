# Generated by Django 4.0 on 2022-03-30 06:48

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='color',
            field=colorfield.fields.ColorField(choices=[('#FFFFFF', 'white'), ('#000000', 'black')], default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
    ]
