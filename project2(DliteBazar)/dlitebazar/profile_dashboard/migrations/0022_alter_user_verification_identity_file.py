# Generated by Django 5.0.6 on 2024-07-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_dashboard', '0021_user_verification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_verification',
            name='identity_file',
            field=models.FileField(upload_to='identity_files/'),
        ),
    ]
