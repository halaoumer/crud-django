# Generated by Django 4.1.4 on 2022-12-30 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachers',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='department',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='lname',
        ),
    ]
