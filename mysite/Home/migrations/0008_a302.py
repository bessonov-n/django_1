# Generated by Django 2.2.5 on 2019-12-05 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_a021_a022_a024'),
    ]

    operations = [
        migrations.CreateModel(
            name='A302',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True)),
                ('val', models.TextField(db_index=True)),
            ],
        ),
    ]
