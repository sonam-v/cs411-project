# Generated by Django 3.1.3 on 2020-11-29 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Podcast',
            new_name='Track',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='podcast',
            new_name='track',
        ),
    ]
