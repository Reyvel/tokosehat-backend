# Generated by Django 2.2.3 on 2019-08-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190830_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='is_served',
            field=models.BooleanField(default=True),
        ),
    ]
