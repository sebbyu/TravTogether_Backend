from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.HyperlinkedModelSerializer):

  # users = serializers.HyperlinkedRelatedField(
  #   many=True, read_only=True, view_name='user-detail', lookup_field='slug',
  # )
  users = serializers.StringRelatedField(
    many=True, read_only=True
  )

  class Meta:
    model = Location
    fields = ('place', 'slug', 'local_map', 'users',)