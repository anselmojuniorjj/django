# Generated by Django 2.2 on 2019-04-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cliente_sobrenome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='idade',
            field=models.IntegerField(max_length=3),
        ),
    ]
