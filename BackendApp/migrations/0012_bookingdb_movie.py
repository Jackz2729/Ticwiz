# Generated by Django 4.1.7 on 2023-06-19 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BackendApp', '0011_bookingdb_rename_show_time_moviedb_show_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdb',
            name='Movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Movie', to='BackendApp.moviedb'),
        ),
    ]
