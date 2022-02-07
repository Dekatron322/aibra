# Generated by Django 3.1.7 on 2022-01-27 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resume', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(default='candidate', max_length=10)),
                ('cprofile_status', models.BooleanField(default=False)),
                ('profile_photo', models.FileField(blank=True, default='default_files/default_face.png', upload_to='account_files/profile_photos/')),
                ('address', models.TextField(default=' ')),
                ('country', models.CharField(default=' ', max_length=20)),
                ('phone_no', models.CharField(default=' ', max_length=10)),
                ('age', models.IntegerField(null=True)),
                ('otp_code', models.CharField(default='none', max_length=10)),
                ('ec_status', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
