# Generated by Django 3.0.1 on 2019-12-20 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20191220_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchquery',
            name='query',
        ),
    ]
