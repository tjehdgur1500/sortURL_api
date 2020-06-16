from django.contrib.auth.models import User
from rest_framework import serializers
from sorten.serializer import SortenSerializer

class UserSerializer(serializers.ModelSerializer):

    urls = SortenSerializer(many=True, read_only=True)

    class Meta :
        model = User
        fields = ('id', 'username', 'password', 'email', 'urls', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(user.password)
        user.save()
        return user