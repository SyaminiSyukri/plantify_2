# Generated by Django 5.1 on 2024-10-24 16:59

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_notes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='image',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='pic/%y/'), upload_to='pic/%y/'),
        ),
    ]
