# Generated by Django 4.0 on 2022-03-27 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_post_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='valus',
        ),
        migrations.AddField(
            model_name='post',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
