# Generated by Django 5.0.6 on 2024-07-10 05:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_dashboard', '0018_alter_purchased_items_purchase_from_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_rating_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_rating', models.IntegerField()),
                ('image_review', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('purchased_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_dashboard.purchased_items')),
            ],
            options={
                'db_table': 'image_review',
            },
        ),
    ]
