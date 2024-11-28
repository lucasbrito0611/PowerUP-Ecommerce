# Generated by Django 5.1 on 2024-11-28 18:51

import loja.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0029_remove_produto_favorito_produto_estoque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='Estoque',
            field=models.IntegerField(default=10, validators=[loja.validators.numero_nao_negativo]),
        ),
        migrations.AlterField(
            model_name='produto',
            name='Preco',
            field=models.FloatField(validators=[loja.validators.numero_nao_negativo]),
        ),
        migrations.AlterField(
            model_name='produto',
            name='Promocao',
            field=models.IntegerField(default=0, null=True, validators=[loja.validators.porcentagem]),
        ),
    ]
