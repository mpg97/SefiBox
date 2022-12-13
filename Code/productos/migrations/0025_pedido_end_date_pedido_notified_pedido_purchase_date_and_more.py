# Generated by Django 4.1.3 on 2022-12-12 21:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0024_pedido_apellidos_pedido_nombre_alter_pedido_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='notified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pedido',
            name='purchase_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='redeemed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pedido',
            name='redemption_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peliculas',
            name='duration',
            field=models.FloatField(default=1.0),
            preserve_default=False,
        ),
    ]