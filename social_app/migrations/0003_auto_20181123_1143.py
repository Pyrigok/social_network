# Generated by Django 2.0 on 2018-11-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0002_auto_20181123_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message_model',
            name='content',
            field=models.CharField(max_length=500, verbose_name='Text of Message'),
        ),
    ]
