# Generated by Django 3.0.4 on 2020-03-17 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptedCrypto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('code', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=10000)),
                ('geolocation', models.CharField(blank=True, max_length=150)),
                ('accepted_cryptos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.AcceptedCrypto')),
            ],
        ),
    ]
