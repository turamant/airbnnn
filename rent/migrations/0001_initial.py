# Generated by Django 4.1 on 2022-08-24 13:11

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
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('email_verified_at', models.DateTimeField(auto_now_add=True)),
                ('passport', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'reservation',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_type', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('has_tv', models.BooleanField()),
                ('has_internet', models.BooleanField()),
                ('has_kitchen', models.BooleanField()),
                ('has_air_condition', models.BooleanField()),
                ('price', models.PositiveIntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.profile')),
            ],
            options={
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('reservation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.reservation')),
            ],
            options={
                'db_table': 'review',
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.room'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.profile'),
        ),
    ]