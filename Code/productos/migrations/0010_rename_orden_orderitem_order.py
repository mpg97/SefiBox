# Generated by Django 4.1.3 on 2022-11-27 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_remove_order_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='orden',
            new_name='order',
        ),
    ]
