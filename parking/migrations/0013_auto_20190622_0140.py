# Generated by Django 2.2.1 on 2019-06-21 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0012_vehicleexit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleexit',
            name='tagno',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
