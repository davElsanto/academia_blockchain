# Generated by Django 3.0.4 on 2020-10-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_contactmethod_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
