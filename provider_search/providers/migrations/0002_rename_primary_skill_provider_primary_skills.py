# Generated by Django 3.2.18 on 2023-03-21 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provider',
            old_name='primary_skill',
            new_name='primary_skills',
        ),
    ]
