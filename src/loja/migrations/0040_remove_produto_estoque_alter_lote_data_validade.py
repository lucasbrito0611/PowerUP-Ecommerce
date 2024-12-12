# Generated by Django 5.1 on 2024-12-12 18:56

import loja.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0039_lote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='estoque',
        ),
        migrations.AlterField(
            model_name='lote',
            name='data_validade',
            field=models.DateField(validators=[loja.validators.data_futura]),
        ),
    ]
