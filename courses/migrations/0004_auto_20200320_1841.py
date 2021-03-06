# Generated by Django 3.0.4 on 2020-03-20 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_acceptedcrypto'),
        ('courses', '0003_course_accepted_cryptos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AcceptedCrypto',
        ),
        migrations.AlterField(
            model_name='course',
            name='accepted_cryptos',
            field=models.ManyToManyField(related_name='accepted_cryptos', to='profiles.AcceptedCrypto'),
        ),
    ]
