from django.contrib.gis.db import models


class Station(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    closing = models.BooleanField(default=False)
    point = models.PointField(
        help_text="Represented as (longitude, latitude)",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=100)
    new = models.BooleanField(default=False)

    objects = models.GeoManager()

    def __str__(self):
        return '({}) {}'.format(self.code, self.name)
