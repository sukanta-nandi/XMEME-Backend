from rest_framework import serializers
from .models import memeData


class memeDataSerializer(serializers.ModelSerializer):
    """Serializes memeData model"""

    class Meta:
        model  = memeData
        fields = ['id','name', 'caption', 'url']