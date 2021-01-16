from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
import os


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):

  image_url = serializers.SerializerMethodField('get_image_url')

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

  def get_image_url(self, obj):
    try:
      request = self.context.get("request")
      full = request.build_absolute_uri(obj.profilePicture.url)
      return full.split('media')[0]+"static/media"+full.split('media')[1]
    except:
      return None  
    
  class Meta:
    model = User
    fields = '__all__'