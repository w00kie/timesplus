from django.db import models

import re


class Booking(models.Model):
    booking_id = models.BigIntegerField(primary_key=True)
    car = models.CharField(max_length=100)
    station_name = models.CharField(max_length=100)
    station = models.ForeignKey(
        'timesdata.Station',
        models.SET_NULL,
        blank=True,
        null=True,
    )
    booking_start = models.DateTimeField('Booking start time')
    booking_end = models.DateTimeField('Booking end time')
    used_start = models.DateTimeField('Usage start time')
    used_end = models.DateTimeField('Usage end time')
    distance = models.IntegerField()
    max_speed = models.IntegerField('Maximum speed')
    sudden_accel = models.IntegerField('Number of sudden accelerations')
    sudden_decel = models.IntegerField('Number of sudder decelerations')
    time_charge = models.IntegerField('Usage time charge')
    distance_charge = models.IntegerField('Driven distance charge')
    penalty_charge = models.IntegerField('Late return penalty charge')
    insurance_charge = models.IntegerField()
    total_charge = models.IntegerField()

    CAR_INFO = re.compile(r'(?P<model>.*) （(?P<plate>.*):(?P<color>.*)）')

    def _get_car_model(self):
        result = CAR_INFO.match(self.car)
        if result:
            return result.group('model')
        else:
            return 'Unknown'
    car_model = property(_get_car_model)

    def _get_car_plate(self):
        result = CAR_INFO.match(self.car)
        if result:
            return result.group('plate')
        else:
            return 'Unknown'
    car_plate = property(_get_car_plate)

    def __str__(self):
        return str(self.booking_id)
