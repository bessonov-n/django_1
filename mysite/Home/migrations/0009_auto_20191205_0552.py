# Generated by Django 2.2.5 on 2019-12-05 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_a302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a302',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='a302',
            name='val',
            field=models.TextField(),
        ),
    ]