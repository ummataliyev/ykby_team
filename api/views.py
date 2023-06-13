from datetime import datetime

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Room
from .models import Booking
from .serializers import RoomSerializer
from .serializers import BookingSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'page': self.page.number,
            'count': self.page.paginator.count,
            'page_size': self.get_page_size(self.request),
            'results': data
        })


class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    pagination_class = CustomPagination


class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    pagination_class = CustomPagination


class RoomAvailabilityAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        room_id = kwargs.get('pk')
        date_param = request.GET.get('date', None)

        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return Response(
                {'error': 'Room not found'},
                status=status.HTTP_404_NOT_FOUND
                )

        if date_param:
            try:
                date = datetime.strptime(date_param, '%d-%m-%Y').date()
            except ValueError:
                return Response(
                    {'error': 'Invalid date format (dd-mm-yyyy format).'},
                    status=status.HTTP_400_BAD_REQUEST
                    )
        else:
            date = datetime.now().date()

        bookings = Booking.objects.filter(room=room, start_time__date=date)

        availability = []
        for booking in bookings:
            availability.append({
                'start': booking.start_time.strftime('%d-%m-%Y %H:%M:%S'),
                'end': booking.end_time.strftime('%d-%m-%Y %H:%M:%S')
            })

        return Response(availability, status=status.HTTP_200_OK)


class BookingCreateAPIView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        room_id = kwargs.get('pk')
        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return Response(
                {'error': 'Room not found'},
                status=status.HTTP_404_NOT_FOUND
                )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        start_time = serializer.validated_data['start_time']
        end_time = serializer.validated_data['end_time']

        if Booking.objects.filter(
            room=room,
            start_time__lt=end_time,
            end_time__gt=start_time).exists():

            return Response(
                {'error': 'Sorry, the room is busy at the time you selected'},
                status=status.HTTP_410_GONE
                )

        booking = Booking(
            room=room,
            resident=serializer.validated_data['resident']['name'],
            start_time=start_time, end_time=end_time
            )

        booking.save()

        return Response(
            {'message': 'Room booked successfully'},
            status=status.HTTP_201_CREATED
            )
