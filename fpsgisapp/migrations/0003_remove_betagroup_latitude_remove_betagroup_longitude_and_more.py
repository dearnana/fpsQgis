# Generated by Django 4.1.3 on 2022-11-21 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fpsgisapp', '0002_remove_betagroup_ein_remove_clientsus_ein_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='betagroup',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='betagroup',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='clientsnonus',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='clientsnonus',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='clientsus',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='clientsus',
            name='longitude',
        ),
    ]
