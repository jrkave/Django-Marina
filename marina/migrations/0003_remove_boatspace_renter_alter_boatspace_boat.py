# Generated by Django 4.2.9 on 2024-02-01 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marina', '0002_boatregistration_boatlicense'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boatspace',
            name='renter',
        ),
        migrations.AlterField(
            model_name='boatspace',
            name='boat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='marina.boat'),
        ),
    ]
