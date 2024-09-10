# Generated by Django 3.2.8 on 2021-12-12 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500, verbose_name='Bio')),
                ('location', models.CharField(blank=True, max_length=30, verbose_name='City')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('avatar_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Profile Photo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Account')),
            ],
        ),
    ]
