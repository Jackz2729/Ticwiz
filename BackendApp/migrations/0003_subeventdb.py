# Generated by Django 4.1.7 on 2023-06-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendApp', '0002_alter_eventcategorydb_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubeventDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Subcategory_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Sub_description', models.CharField(blank=True, max_length=500, null=True)),
                ('Sub_Image', models.ImageField(upload_to='Sub_Cattegory')),
            ],
        ),
    ]
