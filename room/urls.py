from django.urls import path
from .views import RoomListAPIView, RoomDetailAPIView, RoomAvailabilityAPIView, BookingCreateAPIView

urlpatterns = [
    path('rooms', RoomListAPIView.as_view(), name='room-list'),
    path('rooms/<int:pk>', RoomDetailAPIView.as_view(), name='room-detail'),
    path('rooms/<int:pk>/availability', RoomAvailabilityAPIView.as_view(), name='room-availability'),
    path('rooms/<int:pk>/book', BookingCreateAPIView.as_view(), name='booking-create'),
]
