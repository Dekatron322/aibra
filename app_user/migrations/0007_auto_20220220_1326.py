# Generated by Django 3.1.7 on 2022-02-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0006_appuser_agency_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='agency_logo',
            field=models.FileField(blank=True, default='default_files/default_face.png', upload_to='account_files/profile_photos/'),
        ),
    ]
