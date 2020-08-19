from auction.models import Lot
from rest_framework import serializers


class LotSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Lot
        fields = ('creature', 'price', 'user', )


class LotDeepSerializer(serializers.ModelSerializer):
    bets = serializers.StringRelatedField(many=True)

    class Meta:
        model = Lot
        fields = '__all__'
