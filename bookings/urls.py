from django.conf.urls import url
from djgeojson.views import GeoJSONLayerView

from .models import Booking

urlpatterns = [
    url(
        r'^data.geojson$',
        GeoJSONLayerView.as_view(
            model=Booking,
        ),
        name='booked-stations',
    ),
]
