# Generated by Django 4.1.3 on 2022-11-18 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('duracion', models.DurationField()),
                ('fecha', models.DateTimeField()),
                ('genero', models.CharField(max_length=200)),
            ],
        ),
    ]
