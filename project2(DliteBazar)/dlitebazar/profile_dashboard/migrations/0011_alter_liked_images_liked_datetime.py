# Generated by Django 5.0.6 on 2024-07-08 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_dashboard', '0010_alter_liked_images_liked_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liked_images',
            name='liked_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
