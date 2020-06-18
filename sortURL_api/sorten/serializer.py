from rest_framework import serializers
from .models import Sorten


class SortenSerializer(serializers.ModelSerializer):

    shorturl = serializers.ReadOnlyField()
    count = serializers.ReadOnlyField()

    class Meta:
        model = Sorten
        fields = ('id', 'selfurl', 'shorturl', 'count')

