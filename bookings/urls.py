from django.conf.urls import url
from djgeojson.views import GeoJSONLayerView

from . import views
from .models import Booking

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(
        r'^data.geojson$',
        GeoJSONLayerView.as_view(
            model=Booking,
        ),
        name='booked-stations',
    ),
]
