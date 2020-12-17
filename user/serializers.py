from rest_framework import serializers
from django.contrib.auth import get_user_model
from location.serializers import LocationSerializer


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):

  # location = serializers.HyperlinkedRelatedField(
  #     view_name='location-detail', read_only=True, lookup_field='slug',
  #   )

  class Meta:
    model = User
    fields = ('email', 'slug', 'nickname', 'gender', 'race', 'age', 'location',)

  def to_representation(self, instance):
    response = super().to_representation(instance)
    response['location'] = LocationSerializer(instance.location).data
    return self.return_representation(response)
    # return response

  def return_representation(self, response):
    result = {'email': response['email'],
              'slug': response['slug'],
              'nickname': response['nickname'],
              'gender': response['gender'],
              'race': response['race'],
              'age': response['age'],
              'location': response['location']['place']}
    return result