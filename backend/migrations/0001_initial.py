# Generated by Django 3.2.7 on 2021-09-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=50)),
                ('country_cheers', models.IntegerField(default=0)),
            ],
        ),
    ]
