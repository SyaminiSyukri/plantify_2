# Generated by Django 5.1 on 2024-10-30 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_notes_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='image',
            field=models.FileField(default=1, upload_to='pic/%y/'),
            preserve_default=False,
        ),
    ]
