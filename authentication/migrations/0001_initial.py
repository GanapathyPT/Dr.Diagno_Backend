# Generated by Django 3.2 on 2021-04-11 07:22

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
                ('username', models.CharField(max_length=150)),
                ('age', models.SmallIntegerField()),
                ('gender', models.CharField(choices=[('MALE', 0), ('FEMALE', 1), ('OTHER', 2)], max_length=10)),
                ('bloodgroup', models.CharField(max_length=10)),
                ('profile_pic', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]