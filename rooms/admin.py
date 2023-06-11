from django.contrib import admin

from .models import Room
from .models import Booking


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'seats')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'start_time', 'end_time')
