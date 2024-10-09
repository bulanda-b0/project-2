# Generated by Django 5.0.6 on 2024-07-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0002_user_registration_reward_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_registration',
            name='reward_points',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
