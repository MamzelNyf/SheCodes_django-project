# Generated by Django 3.0.8 on 2020-08-16 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20200814_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='category',
            field=models.ForeignKey(default='Design', on_delete=django.db.models.deletion.SET_DEFAULT, to='news.Category'),
        ),
    ]
