# Generated by Django 4.1.3 on 2022-12-03 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0020_escaparates_fecha_modificación'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escaparates',
            name='fecha_modificación',
        ),
        migrations.AddField(
            model_name='escaparates',
            name='mostrar',
            field=models.BooleanField(default=False),
        ),
    ]
