# Generated by Django 4.1 on 2022-08-26 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_alter_reservation_room_id'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='profile',
            table='users',
        ),
        migrations.AlterModelTable(
            name='reservation',
            table='reservations',
        ),
        migrations.AlterModelTable(
            name='review',
            table='reviews',
        ),
        migrations.AlterModelTable(
            name='room',
            table='rooms',
        ),
    ]
