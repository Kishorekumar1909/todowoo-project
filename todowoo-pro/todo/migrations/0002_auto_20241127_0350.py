# Generated by Django 3.2.25 on 2024-11-26 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='completed',
            new_name='datecompleted',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='tittle',
            new_name='title',
        ),
    ]
