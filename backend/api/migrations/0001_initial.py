# Generated by Django 5.1.1 on 2024-11-07 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('number_of_stations', models.IntegerField()),
                ('available_on_weekend', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='LineStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('notes', models.TextField(blank=True)),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.line')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.station')),
            ],
        ),
        migrations.AddField(
            model_name='line',
            name='stations',
            field=models.ManyToManyField(through='api.LineStation', to='api.station'),
        ),
    ]
