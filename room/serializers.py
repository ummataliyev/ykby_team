from rest_framework import serializers
from .models import Room
from .models import Booking


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'number', 'category', 'seats']


class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = ['user', 'room', 'start_time', 'end_time']
