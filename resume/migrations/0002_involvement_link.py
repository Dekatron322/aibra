# Generated by Django 3.1.7 on 2022-01-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='involvement',
            name='link',
            field=models.CharField(default='#', max_length=50),
        ),
    ]
