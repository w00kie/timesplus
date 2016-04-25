from django.db import models


class Station(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    closing = models.BooleanField(default=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    name = models.CharField(max_length=100)
    new = models.BooleanField(default=False)

    def __str__(self):
        return '({}) {}'.format(self.code, self.name)
