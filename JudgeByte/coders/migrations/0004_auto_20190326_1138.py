# Generated by Django 2.1.7 on 2019-03-26 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coders', '0003_auto_20190324_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='handle',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='registeredDate',
        ),
    ]
