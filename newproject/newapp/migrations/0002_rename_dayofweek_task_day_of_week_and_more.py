# Generated by Django 5.0.3 on 2024-05-02 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='dayofweek',
            new_name='day_of_week',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='peoplenumber',
            new_name='number_of_people',
        ),
    ]