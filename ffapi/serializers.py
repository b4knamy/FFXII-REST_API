from rest_framework import serializers
from .models import Character, Esper

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:

        model = Character
        fields = '__all__'


class EsperSerializer(serializers.ModelSerializer):
    class Meta:

        model = Esper
        fields = '__all__'
