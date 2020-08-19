from auction.models import Bet
from rest_framework import generics
from rest_framework import exceptions
from auction.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from auction.serializers.bet_serializers import BetSerializer, BetListSerializer, \
    BetSelectSerializer, BetUpdateSerializer


class BetCreateView(generics.CreateAPIView):
    serializer_class = BetSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        queryset = Bet.objects.filter(lot=serializer.validated_data['lot'],
                                      user=serializer.validated_data['user'])
        user_bets = self.filter_queryset(queryset)
        if len(user_bets) > 0:
            raise exceptions.PermissionDenied(
                detail='Not allowed to create multiple bets per lot for 1 user.')

        serializer.save()


class BetListView(generics.ListAPIView):
    serializer_class = BetListSerializer
    queryset = Bet.objects.all()
    permission_classes = (IsAuthenticated, )


class BetUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = BetUpdateSerializer
    queryset = Bet.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


class BetSelectView(generics.RetrieveUpdateAPIView):
    serializer_class = BetSelectSerializer
    queryset = Bet.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )

    def get_object(self):
        bet = self.filter_queryset(queryset=self.queryset).get(pk=self.kwargs[self.lookup_field])
        self.check_object_permissions(self.request, bet.lot)

        selected_bets = self.filter_queryset(queryset=self.queryset).filter(lot=bet.lot, selected=True)\
            .exclude(id=bet.id)
        if len(selected_bets) > 0:
            raise exceptions.PermissionDenied(
                detail='Not allowed to select multiple bets.')
        return bet
