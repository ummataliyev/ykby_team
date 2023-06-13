from django.db import models


class Room(models.Model):
    ROOM_TYPE = (
        ('VIP', 'for conference'),
        ('PREMIUM', 'for team'),
        ('SILVER', 'for focus'),
    )

    number = models.IntegerField()
    category = models.CharField(max_length=10, choices=ROOM_TYPE)
    seats = models.IntegerField()

    def __str__(self):
        return f'{self.number}, {self.category} with {self.seats} seats'


class Booking(models.Model):
    resident = models.CharField(max_length=255)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"User: {self.resident}, Room: {self.room}, Start Time: {self.start_time}, End Time: {self.end_time}" # noqa
