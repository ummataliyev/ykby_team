from rest_framework import serializers

from .models import Room
from .models import Booking


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'number', 'category', 'seats']


class BookingSerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    resident = serializers.CharField(source='resident.name')

    start_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    end_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Booking
        fields = ['resident', 'room', 'start_time', 'end_time']
