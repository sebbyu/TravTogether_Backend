from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
import socket
import urllib



User = get_user_model()
class UserSerializer(serializers.ModelSerializer):

  def create(self, validated_data):
    user = User(
      **validated_data,
    )
    user.is_active = True
    user.set_password(validated_data['password'])
    user.save()
    return user

  def update(self, instance, validated_data):
    instance.email = validated_data.get('email', instance.email)
    instance.nickname = validated_data.get('nickname', instance.nickname)
    instance.gender = validated_data.get('gender', instance.gender)
    instance.age = validated_data.get('age', instance.age)
    instance.ethnicity = validated_data.get('ethnicity', instance.ethnicity)
    instance.location = validated_data.get('location', instance.location)
    instance.bio = validated_data.get('bio', instance.bio)
    password = validated_data.pop('password')
    if password != instance.password:
      instance.set_password(password)
    instance.save()
    return instance

  class Meta:
    model = User
    fields = '__all__'

  # def to_representation(self, instance):
  #   response = super().to_representation(instance)
  #   response['location'] = LocationSerializer(instance.location).data
  #   return self.return_representation(response)
  #   return response

  # def return_representation(self, response):
  #   result = {'email': response['email'],
  #             'slug': response['slug'],
  #             'profile_picture': response['profile_picture'],
  #             'nickname': response['nickname'],
  #             'gender': response['gender'],
  #             'race': response['race'],
  #             'age': response['age'],
  #             'location': response['location']['place'],
  #             'bio': response['bio']}
  #   return result