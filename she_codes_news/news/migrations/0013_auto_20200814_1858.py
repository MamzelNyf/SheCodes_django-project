# Generated by Django 3.0.8 on 2020-08-14 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20200814_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='category',
            field=models.TextField(default=None, max_length=128),
        ),
    ]
