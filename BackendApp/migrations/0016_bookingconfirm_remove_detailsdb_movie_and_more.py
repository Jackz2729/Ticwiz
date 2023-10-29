# Generated by Django 4.1.7 on 2023-07-02 08:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendApp', '0015_alter_bookingdb_time_alter_detailsdb_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingConfirm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Seat', models.CharField(blank=True, max_length=50, null=True)),
                ('Movie', models.CharField(blank=True, max_length=100, null=True)),
                ('Screen', models.CharField(blank=True, max_length=100, null=True)),
                ('Time', models.CharField(blank=True, max_length=100, null=True)),
                ('Date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.RemoveField(
            model_name='detailsdb',
            name='Movie',
        ),
        migrations.RemoveField(
            model_name='detailsdb',
            name='Screen',
        ),
        migrations.RemoveField(
            model_name='detailsdb',
            name='Seat',
        ),
        migrations.RemoveField(
            model_name='detailsdb',
            name='Time',
        ),
    ]