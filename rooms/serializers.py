from rest_framework import serializers

from .models import Room
from .models import Booking


class RoomSerializer(serializers.Serializer):
    class Meta:
        model = Room
        fields = '__all__'


class BookingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
