# Generated by Django 2.0 on 2018-11-23 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message_model',
            old_name='text',
            new_name='content',
        ),
    ]
