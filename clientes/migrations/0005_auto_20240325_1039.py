# Generated by Django 3.0.8 on 2024-03-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20240325_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]