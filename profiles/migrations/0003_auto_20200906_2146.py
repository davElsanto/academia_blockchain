# Generated by Django 3.0.4 on 2020-09-06 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_acceptedcrypto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_accreditor',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
