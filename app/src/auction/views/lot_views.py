from auction.models import Lot
from rest_framework import generics
from rest_framework import exceptions
from auction.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from auction.serializers.lot_serializers import LotSerializer, LotDeepSerializer


class LotCreateView(generics.CreateAPIView):
    serializer_class = LotSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        if serializer.validated_data['creature'].user != self.request.user:
            raise exceptions.PermissionDenied(
                detail='You do not have permission')

        serializer.save()


class LotListView(generics.ListAPIView):
    serializer_class = LotDeepSerializer
    queryset = Lot.objects.all()
    permission_classes = (IsAuthenticated, )


class LotDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = LotDeepSerializer
    queryset = Lot.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
