# Generated by Django 5.0.6 on 2024-07-08 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_dashboard', '0008_support_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='liked_images',
            name='liked_datetime',
            field=models.DateField(blank=True, null=True),
        ),
    ]
