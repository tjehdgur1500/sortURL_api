from rest_framework import serializers
from .models import Sorten


class SortenSerializer(serializers.ModelSerializer):

    count = serializers.ReadOnlyField()
    responseurl = serializers.ReadOnlyField()

    class Meta:
        model = Sorten
        fields = ('id', 'selfurl', 'responseurl', 'count')

