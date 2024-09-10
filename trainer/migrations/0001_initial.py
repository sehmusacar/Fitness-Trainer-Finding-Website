# Generated by Django 4.0 on 2021-12-12 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('Surname', models.CharField(max_length=120)),
                ('City', models.CharField(max_length=120)),
                ('Phone', models.CharField(max_length=10)),
                ('Mail', models.EmailField(max_length=120)),
                ('Gender', models.BooleanField(choices=[(True, 'Erkek'), (False, 'Kadın')])),
                ('Address', models.TextField()),
                ('Work_Experience', models.TextField()),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('Birth_Date', models.DateField()),
                ('is_approved', models.BooleanField(choices=[(True, 'Onaylı'), (False, 'Onaylanmamış')], default=False, verbose_name='Onay')),
                ('User_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainers', to='auth.user', verbose_name='Kullanıcı Hesabı')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Başlık')),
                ('content', models.TextField(verbose_name='Yorum')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='trainer.trainer', verbose_name='Gönderi')),
            ],
        ),
    ]
