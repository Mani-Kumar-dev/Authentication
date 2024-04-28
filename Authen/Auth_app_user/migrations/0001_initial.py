# Generated by Django 5.0.4 on 2024-04-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request_details',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('number', models.BigIntegerField()),
            ],
        ),
    ]