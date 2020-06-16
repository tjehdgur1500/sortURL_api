from rest_framework import serializers
from .models import Sorten


class SortenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sorten
        fields = ('id', 'selfurl',)