from django.shortcuts import render
from django.db.models import Count

from timesdata.models import Station


def dashboard(request):
    context = {
        'stations': Station.objects.all().annotate(nb_bookings=Count('bookings__booking_id')).filter(nb_bookings__gt=0).order_by('-nb_bookings'),
    }
    return render(request, 'bookings/dashboard.html', context)
