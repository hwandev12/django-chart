# Generated by Django 4.0 on 2022-03-30 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_line'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='date',
            field=models.CharField(max_length=40),
        ),
    ]
