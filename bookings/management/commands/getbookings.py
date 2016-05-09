from django.core.management.base import BaseCommand, CommandError
from django.utils.dateparse import parse_datetime

from bookings.models import Booking

import requests
import csv
import re
import pytz

CSV_URL = 'https://docs.google.com/spreadsheets/d/1vqZR2e8ed2kt4dXgyR-D1fm9Ji5lspTYwqZVDfVGk-c/pub?gid=0&single=true&output=csv'


def match(regexp, string, default):
    m = re.match(regexp, string)
    if m:
        return m.group(0)
    else:
        return default


def tzaware(naive, tz='Asia/Tokyo'):
    naive = parse_datetime(naive.replace('/', '-'))
    return pytz.timezone(tz).localize(naive)


class Command(BaseCommand):
    help = 'Download and parse bookings from published CSV'

    def handle(self, *args, **options):
        # Get all the existing ids
        all_bookings = Booking.objects.all().values_list('pk', flat=True)

        # Download the CSV and parse it
        r = requests.get(CSV_URL)
        # Force encoding because it's a bitch
        r.encoding = 'utf-8'
        bookings = csv.DictReader(r.text.splitlines())
        bookings_to_create = []
        for booking in bookings:
            if int(booking['booking_id']) not in all_bookings:
                new_booking = Booking(
                    booking_id=booking['booking_id'],
                    car=booking['car'],
                    station_name=booking['station'],
                    booking_start=tzaware(booking['booking_time'].split(' - ')[0]),
                    booking_end=tzaware(booking['booking_time'].split(' - ')[1]),
                    used_start=tzaware(booking['used_time'].split(' - ')[0]),
                    used_end=tzaware(booking['used_time'].split(' - ')[1]),
                    distance=match(r'\d+', booking['distance'], 0),
                    max_speed=match(r'\d+', booking['max_speed'], 0),
                    sudden_accel=match(r'\d+', booking['sudden_accel'], 0),
                    sudden_decel=match(r'\d+', booking['sudden_decel'], 0),
                    time_charge=match(r'[\d,]+', booking['time_charge'], '0').replace(',', ''),
                    distance_charge=match(r'[\d,]+', booking['distance_charge'], '0').replace(',', ''),
                    penalty_charge=match(r'[\d,]+', booking['penalty_charge'], '0').replace(',', ''),
                    insurance_charge=match(r'[\d,]+', booking['insurance_charge'], '0').replace(',', ''),
                    discount=match(r'[-\d,]+', booking['discount'], '0').replace(',', ''),
                    total_charge=match(r'[\d,]+', booking['total_charge'], '0').replace(',', ''),
                )
                bookings_to_create.append(new_booking)
        Booking.objects.bulk_create(bookings_to_create)

        self.stdout.write(
            self.style.SUCCESS('Successfully retrieved {} new bookings'.format(len(bookings_to_create)))
        )
