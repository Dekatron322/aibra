# Generated by Django 3.1.7 on 2022-01-27 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='decription',
            new_name='description',
        ),
    ]
