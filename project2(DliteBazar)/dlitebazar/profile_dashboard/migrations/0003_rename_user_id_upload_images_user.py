# Generated by Django 5.0.6 on 2024-07-05 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_dashboard', '0002_rename_user_upload_images_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload_images',
            old_name='user_id',
            new_name='user',
        ),
    ]
