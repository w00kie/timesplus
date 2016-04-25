from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import MultipleObjectsReturned

from bookings.models import Booking
from timesdata.models import Station


class Command(BaseCommand):
    help = 'Match bookings with their related stations'

    def handle(self, *args, **options):
        for m in Booking.objects.all().filter(station=None):
            try:
                station = Station.objects.get(name=m.station_name)
                m.station = station
                m.save()
            except Station.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING('Could not find station named {}'.format(m.station_name))
                )
            except MultipleObjectsReturned:
                self.stdout.write(
                    self.style.WARNING('Ambiguous: found multiple stations named {}'.format(m.station_name))
                )
