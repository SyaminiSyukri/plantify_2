# Generated by Django 5.1 on 2024-10-19 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_member'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member',
            new_name='Notes',
        ),
    ]