# Generated by Django 3.2.5 on 2021-07-11 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlevendas', '0002_auto_20210711_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='valorTotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Valor total do Pedido'),
        ),
    ]
