# Generated by Django 2.2 on 2019-04-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190404_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
