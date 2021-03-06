# Generated by Django 3.2.7 on 2021-09-08 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_sport', models.CharField(max_length=50)),
                ('event_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.country')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.event')),
            ],
        ),
        migrations.CreateModel(
            name='Medal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medal_type', models.CharField(default='', max_length=8)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.country')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.event')),
            ],
        ),
    ]
