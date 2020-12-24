from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):

  # profilePicture = serializers.ImageField(
  #   use_url=True,
  # )

  class Meta:
    model = User
    fields = ('email', 'slug', 'profilePicture', 'nickname', 'gender', 
    'ethnicity', 'age', 'location','bio','password')

  def create(self, validated_data):
    user = User(
      **validated_data,
    )
    user.set_password(validated_data['password'])
    user.save()
    return user

  def update(self, instance, validated_data):
    password = validated_data.pop('password')
    instance.email = validated_data.get('email', instance.email)
    instance.nickname = validated_data.get('nickname', instance.nickname)
    instance.gender = validated_data.get('gender', instance.gender)
    instance.ethnicity = validated_data.get('ethnicity', instance.ethnicity)
    instance.age = validated_data.get('age', instance.age)
    instance.location = validated_data.get('location', instance.location)
    instance.bio = validated_data.get('bio', instance.bio)
    if password != None:
      instance.set_password(password)
    instance.save()
    return instance

  # instance.email = validated_data.get('email', instance.email)
  #       instance.content = validated_data.get('content', instance.content)
  #       instance.created = validated_data.get('created', instance.created)


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