# Generated by Django 2.2 on 2019-04-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190404_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='sobrenome',
            field=models.CharField(default='', max_length=70),
            preserve_default=False,
        ),
    ]
