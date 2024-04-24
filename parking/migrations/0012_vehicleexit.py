# Generated by Django 2.2.1 on 2019-06-21 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0011_auto_20190620_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicleexit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vnumber', models.CharField(max_length=10)),
                ('vtype', models.CharField(choices=[('two', 'Two Wheeler'), ('three', 'Three Wheeler'), ('four', 'Four Wheeler')], default='two', max_length=10)),
                ('outtime', models.TimeField(blank=True, null=True)),
                ('tagno', models.CharField(max_length=10)),
            ],
        ),
    ]
