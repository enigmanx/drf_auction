from rest_framework import generics
from auction.models import Creature
from auction.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from auction.serializers.creature_serializers import CreatureDetailSerializer, CreatureListSerializer


class CreatureCreateView(generics.CreateAPIView):
    serializer_class = CreatureDetailSerializer
    permission_classes = (IsAuthenticated, )


class CreatureListView(generics.ListAPIView):
    serializer_class = CreatureListSerializer
    queryset = Creature.objects.all()
    permission_classes = (IsAuthenticated, )


class CreatureDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CreatureDetailSerializer
    queryset = Creature.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
