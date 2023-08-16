# Generated by Django 4.2.4 on 2023-08-16 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargoease', '0004_carrier_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrier',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]