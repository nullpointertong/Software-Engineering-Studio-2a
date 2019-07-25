# Generated by Django 2.1.7 on 2019-05-31 23:28

from django.db import migrations, models
import helps_admin.models


class Migration(migrations.Migration):

    dependencies = [
        ('helps_admin', '0006_auto_20190526_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='end_dates',
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='start_dates',
        ),
        migrations.AddField(
            model_name='workshop',
            name='days',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='workshop',
            name='end_date',
            field=models.DateField(default=helps_admin.models.default_start_time),
        ),
        migrations.AddField(
            model_name='workshop',
            name='end_time',
            field=models.TimeField(default=helps_admin.models.default_start_time),
        ),
        migrations.AddField(
            model_name='workshop',
            name='no_of_sessions',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='workshop',
            name='start_date',
            field=models.DateField(default=helps_admin.models.default_start_time),
        ),
        migrations.AddField(
            model_name='workshop',
            name='start_time',
            field=models.TimeField(default=helps_admin.models.default_start_time),
        ),
    ]