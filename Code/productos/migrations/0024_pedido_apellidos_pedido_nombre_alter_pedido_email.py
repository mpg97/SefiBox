# Generated by Django 4.1.3 on 2022-12-09 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0023_pedido_elementopedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='apellidos',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='pedido',
            name='nombre',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='email',
            field=models.CharField(default=False, max_length=255),
        ),
    ]
