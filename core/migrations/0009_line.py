# Generated by Django 4.0 on 2022-03-30 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_user_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('value', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Line',
                'verbose_name_plural': 'My Lines',
            },
        ),
    ]
