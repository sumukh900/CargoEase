# Generated by Django 4.2.4 on 2023-08-16 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargoease', '0003_container_route'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('breadth', models.DecimalField(decimal_places=2, max_digits=10)),
                ('height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('carrier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargoease.carrier')),
                ('container_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargoease.container')),
                ('route_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargoease.route')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargoease.user')),
            ],
        ),
    ]