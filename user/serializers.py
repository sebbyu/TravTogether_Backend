from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from django.forms.models import model_to_dict
import os


User = get_user_model()

class MessageField(serializers.RelatedField):
  def to_representation(self, value):
    rep = dict()
    dict_model = model_to_dict(value)
    rep['subject'] = dict_model['subject']
    rep['sender'] = dict_model['sender']
    rep['message'] = dict_model['message']
    rep['created'] = dict_model['created'].strftime("%m-%d-%Y %H:%M:%S")
    return rep


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
    try:
      profilePicture = validated_data.pop('profilePicture')
      instance.profilePicture.delete()
      instance.profilePicture = profilePicture
      image_url = validated_data.pop('profilePicture')
      instance.image_url.delete()
      instance.image_url = image_url
    except KeyError:
      pass
    instance.profilePicture = validated_data.get('profilePicture', instance.profilePicture)
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

  # messages = serializers.RelatedField(many=True, read_only=True)
  messages = MessageField(many=True, read_only=True)

  class Meta:
    model = User
    fields = '__all__'