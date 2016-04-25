from django.core.management.base import BaseCommand, CommandError

from timesdata.models import Station

import requests

STATION_API = 'http://plus.timescar.jp/view/station/teeda.ajax'

payload = {
    'component': 'station_stationMapPage',
    'action': 'ajaxViewMap',
    # Bounding box for all of Japan
    'minlat': 20.21,
    'maxlat': 45.71,
    'minlon': 122.71,
    'maxlon': 154.21,
}


class Command(BaseCommand):
    help = 'Scrape all stations information in Japan'

    def handle(self, *args, **opts):
        try:
            s = requests.Session()
            r = s.get(STATION_API, params=payload)
        except requests.ConnectionError:
            raise CommandError('Could not connect to Times Plus server')
        except requests.Timeout:
            raise CommandError('Timeout connecting to Times Plus server')

        stations = r.json()['s']
        self.stdout.write(self.style.SUCCESS(
            'Found {} stations from API'.format(stations.len())
        ))

        count_created = 0
        count_updated = 0
        for station in stations:
            obj, created = Station.objects.update_or_create(
                code=station['cd'],
                defaults={
                    'closing': station['cl'],
                    'lat': station['la'],
                    'lon': station['lo'],
                    'name': station['nm'],
                    'new': station['op'],
                }
            )
            if created:
                count_created = count_created + 1
            else:
                count_updated = count_updated + 1
        self.stdout.write(
            self.style.SUCCESS(
                'Successfully updated {} and created {} stations'.format(
                    count_updated,
                    count_created,
                )
            )
        )
