from auction.models import Creature
from rest_framework import serializers


class CreatureDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Creature
        fields = '__all__'


class CreatureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creature
        fields = '__all__'
