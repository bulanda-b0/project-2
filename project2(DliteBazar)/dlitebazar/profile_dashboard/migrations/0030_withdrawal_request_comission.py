# Generated by Django 5.0.6 on 2024-07-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_dashboard', '0029_purchased_items_paid_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawal_request',
            name='comission',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
