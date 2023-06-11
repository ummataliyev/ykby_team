from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=120)
    room_type = models.CharField(max_length=120)
    seats = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateField(null=True)
    end_time = models.DateField(null=True)

    def __str__(self):
        return f"Booking for room: {self.room}\n- Start time: {self.start_time}\n- End time: {self.end_time}" # noqa
