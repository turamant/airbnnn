'''Airbnb
Упрощенная схема сервиса для сдачи жилья в аренду
    Profile(Users) - Пользователи сервиса
    Reservations - История бронирования жилья
    Rooms - Доступное жильё для аренды
    Reviews - Отзывы на арендуемое жилье
'''
from django.contrib.auth.models import User

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

ROOM_CHOICES = (
    ('K', 'kvartira'),
    ('R', 'room'),
    ('H', 'house')
)


class Profile(models.Model):
    '''User - сущность клиент'''

    class Meta:
        db_table = 'user'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    email_verified_at = models.DateTimeField(auto_now_add=True)
    passport = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Room(models.Model):
    '''Room - сущность арендное жилье'''

    class Meta:
        db_table = 'room'

    home_type = models.CharField(choices=ROOM_CHOICES, max_length=1)
    address = models.CharField(max_length=100)
    has_tv = models.BooleanField()
    has_internet = models.BooleanField()
    has_kitchen = models.BooleanField()
    has_air_condition = models.BooleanField()
    price = models.PositiveIntegerField()
    owner_id = models.ForeignKey(Profile,
                                 on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.address


class Reservation(models.Model):
    '''Reservation - История бронирования жилья'''

    class Meta:
        db_table = 'reservation'

    user_id = models.ForeignKey(Profile,
                                on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, related_name='reservators',
                                on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.PositiveIntegerField()
    total = models.PositiveIntegerField()

    def __str__(self):
        return self.room_id.address

class Review(models.Model):
    '''Review - отзывы на арендное жилье'''

    class Meta:
        db_table = 'review'
    reservation_id = models.ForeignKey(Reservation,
                                       on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return str(self.rating)
