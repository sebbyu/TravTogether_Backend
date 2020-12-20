from rest_framework import serializers
from django.contrib.auth import get_user_model
from location.serializers import LocationSerializer


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):

  # location = serializers.HyperlinkedRelatedField(
  #     view_name='location-detail', read_only=True, lookup_field='slug',
  #   )
  # profile_picture = serializers.ImageField(
  #   allow_empty_file=False,
  #   use_url=False,
  # )

  class Meta:
    model = User
    fields = ('email', 'slug', 'profile_picture', 'nickname', 'gender', 
    'race', 'age', 'location','bio')

  def to_representation(self, instance):
    response = super().to_representation(instance)
    response['location'] = LocationSerializer(instance.location).data
    return self.return_representation(response)
    # return response

  def return_representation(self, response):
    result = {'email': response['email'],
              'slug': response['slug'],
              'profile_picture': response['profile_picture'],
              'nickname': response['nickname'],
              'gender': response['gender'],
              'race': response['race'],
              'age': response['age'],
              'location': response['location']['place'],
              'bio': response['bio']}
    return result