# Generated by Django 3.0.4 on 2020-09-21 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_auto_20200320_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionPlatform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('url_link', models.URLField(blank=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_reccurrent', models.BooleanField(default=False, null=True)),
                ('is_recorded', models.BooleanField(default=False, null=True)),
                ('event_type', models.CharField(blank=True, choices=[('COURSE', 'Curso'), ('CONFERENCE', 'Conferencia')], max_length=50)),
                ('title', models.CharField(blank=True, max_length=150)),
                ('description', models.CharField(blank=True, max_length=10000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_start', models.DateTimeField(blank=True, null=True)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('date_recorded', models.DateTimeField(null=True)),
                ('schedule_description', models.CharField(blank=True, max_length=1000)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('platform', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.ConnectionPlatform')),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
