from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Station

admin.site.register(Station, LeafletGeoAdmin)
