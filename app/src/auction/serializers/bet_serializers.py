from auction.models import Bet
from rest_framework import serializers


class BetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Bet
        fields = ('lot', 'price', 'user', )


class BetUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bet
        fields = ('price', )


class BetListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bet
        fields = '__all__'


class BetSelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bet
        fields = ('selected', )
