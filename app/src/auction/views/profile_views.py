from auction.models import Profile
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from auction.serializers.profile_serializers import ProfileDetailSerializer


class ProfileAdminDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileDetailSerializer
    queryset = Profile.objects.all()
    permission_classes = (IsAdminUser, )


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileDetailSerializer
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj
