# Generated by Django 3.0.8 on 2020-08-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200813_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
