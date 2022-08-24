from django.contrib import admin

from rent.models import Review, Reservation, Room, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email',
                    'email_verified_at', 'passport',
                    'phone_number']


admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Review)
