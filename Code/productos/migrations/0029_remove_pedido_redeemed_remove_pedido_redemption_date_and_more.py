# Generated by Django 4.1.3 on 2022-12-13 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0028_remove_pedido_purchase_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='redeemed',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='redemption_date',
        ),
        migrations.AddField(
            model_name='elementopedido',
            name='redeemed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='elementopedido',
            name='redemption_date',
            field=models.DateTimeField(null=True),
        ),
    ]