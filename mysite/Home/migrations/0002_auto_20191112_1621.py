# Generated by Django 2.2.5 on 2019-11-12 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ikntprofils',
            name='number',
        ),
        migrations.RemoveField(
            model_name='ikntprofils',
            name='val',
        ),
    ]
