# Generated by Django 3.2.13 on 2022-06-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20220606_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecast_master',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]