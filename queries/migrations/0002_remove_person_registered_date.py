# Generated by Django 3.0.8 on 2020-07-29 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='registered_date',
        ),
    ]
