from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Room
from .serializers import RoomSerializer


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
