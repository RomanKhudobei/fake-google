# Generated by Django 3.0.1 on 2019-12-20 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20191220_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchQueries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shown', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='search.RandomText', verbose_name='search_queries')),
            ],
        ),
    ]
