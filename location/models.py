from django.db import models
from django.conf import settings
from location_field.models.plain import PlainLocationField
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
import csv
import os


def get_locations(filename):
  places = []
  with open(filename, encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
      place = ""
      if row[6] in ['CHN', 'USA', 'RUS']:
        place = f'{row[0]}, {row[4]}, {row[1]}'
      else:
        place = f'{row[0]}, {row[1]}'
      places.append((place, place))
    return tuple(places)

PLACES = get_locations(os.path.abspath(os.path.join(settings.STATIC_ROOT,
      'locations/worldcities.csv')))

class Location(models.Model):
  place = models.CharField(_("place"), max_length=100, choices=PLACES)
  slug = models.SlugField(_("slug"), unique=True)
  local_map = PlainLocationField(based_fields=['place'], zoom=4)

  class Meta:
    ordering = ('place',)

  def __str__(self):
    return f'{self.place}'

  def save(self, *args, **kwargs):
    self.slug = slugify(self.place)
    super(Location, self).save(*args, **kwargs)
