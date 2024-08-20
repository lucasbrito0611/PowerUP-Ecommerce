# Generated by Django 5.1 on 2024-08-20 12:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0005_remove_cliente_cep_remove_cliente_endereco_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('Preco', models.FloatField()),
                ('Descricao', models.CharField(max_length=300)),
                ('Dt_fabricacao', models.DateField(default=datetime.date(2000, 1, 1))),
                ('Dt_validade', models.DateField(default=datetime.date(2000, 1, 1))),
            ],
        ),
    ]
